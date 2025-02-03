import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import altair as alt

# Function to calculate the minimum runways needed based on arrival and departure times
def minimum_runways(arrivals, departures, types):
    commercial_arrivals = []
    commercial_departures = []
    extra_runways = 0

    for i in range(len(types)):
        if types[i].lower() in ["private", "military"]:
            extra_runways += 1  # Separate runway for each private or military flight
        else:
            commercial_arrivals.append(arrivals[i])
            commercial_departures.append(departures[i])

    commercial_arrivals.sort()
    commercial_departures.sort()

    max_runways_needed = 0
    i, j, current_runways = 0, 0, 0

    while i < len(commercial_arrivals) and j < len(commercial_departures):
        if commercial_arrivals[i] < commercial_departures[j]:
            current_runways += 1
            max_runways_needed = max(max_runways_needed, current_runways)
            i += 1
        else:
            current_runways -= 1
            j += 1

    total_runways_needed = max_runways_needed + extra_runways
    return total_runways_needed

# Streamlit GUI
st.title("Airplane Runway Scheduling System")

# Input form for flight details
st.header("Enter Flight Details")

num_flights = st.number_input("Enter the number of flights to schedule:", min_value=1, max_value=20, step=1)

# List to store flight details
flights_data = []

# Input section for each flight
for i in range(num_flights):
    st.subheader(f"Flight {i + 1}")
    arrival_time = st.text_input(f"Arrival time for Flight {i + 1} (HH:MM):", key=f"arrival_{i}")
    departure_time = st.text_input(f"Departure time for Flight {i + 1} (HH:MM):", key=f"departure_{i}")
    flight_type = st.selectbox(f"Flight type for Flight {i + 1}:", ["Commercial", "Private", "Military"], key=f"type_{i}")
    flight_class = st.selectbox(f"Class for Flight {i + 1}:", ["Economy", "Premium Economy", "Business", "Private"], key=f"class_{i}")
    
    if arrival_time and departure_time:
        try:
            # Validate time format
            datetime.strptime(arrival_time, "%H:%M")
            datetime.strptime(departure_time, "%H:%M")
            flights_data.append([arrival_time, departure_time, flight_type, flight_class])
        except ValueError:
            st.error("Please enter a valid time format (HH:MM).")

# Button to save data to file and calculate runways
if st.button("Schedule Flights"):
    if not flights_data:
        st.error("Please enter flight details before scheduling.")
    else:
        # Save flights data to file
        df = pd.DataFrame(flights_data, columns=["Arrival", "Departure", "Type", "Class"])
        df.to_csv("flights_schedule.csv", index=False)
        st.success("Flight details saved to 'flights_schedule.csv'.")

        # Prepare data for calculation
        arrivals = [data[0] for data in flights_data]
        departures = [data[1] for data in flights_data]
        types = [data[2] for data in flights_data]

        # Calculate required runways
        total_runways_needed = minimum_runways(arrivals, departures, types)
        st.header(f"Total Runways Needed: {total_runways_needed}")
        
        # Display data in a table
        st.subheader("Flight Schedule")
        st.write(df)

        # Prepare timeline data
        timeline_data = []
        for idx, (arrival, departure, flight_type) in enumerate(zip(arrivals, departures, types)):
            arrival_dt = datetime.strptime(arrival, "%H:%M")
            departure_dt = datetime.strptime(departure, "%H:%M")
            current_time = arrival_dt
            while current_time <= departure_dt:
                timeline_data.append({
                    'Time': current_time,
                    'Flight': f'Flight {idx + 1}',
                    'Runway Status': "Occupied" if flight_type.lower() in ["commercial"] else "Reserved",
                    'Flight Type': flight_type
                })
                current_time += timedelta(minutes=1)

        # Convert to DataFrame for Altair visualization
        timeline_df = pd.DataFrame(timeline_data)

        # Create Altair chart
        chart = alt.Chart(timeline_df).mark_bar().encode(
            x=alt.X('Time:T', title="Time", axis=alt.Axis(format="%H:%M")),
            y=alt.Y('Flight', title="Flight"),
            color=alt.Color('Runway Status', scale=alt.Scale(domain=["Occupied", "Reserved"], range=["red", "blue"]), title="Runway Status"),
            tooltip=['Time', 'Runway Status', 'Flight Type']
        ).properties(
            width=700,
            height=300,
            title="Runway Usage Timeline"
        )

        # Display the chart
        st.altair_chart(chart, use_container_width=True)