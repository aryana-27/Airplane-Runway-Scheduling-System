# Airplane Runway Scheduling System

This project is a Streamlit-based web application designed to help airport authorities schedule flights and determine the minimum number of runways required based on flight arrival and departure times. The system also visualizes runway usage over time using an interactive timeline chart.

## Features

- **Flight Scheduling**: Users can input flight details, including arrival time, departure time, flight type (Commercial, Private, Military), and class (Economy, Premium Economy, Business, Private).
- **Runway Calculation**: The system calculates the minimum number of runways needed to handle all scheduled flights, considering that private and military flights require separate runways.
- **Data Export**: Flight details are saved to a CSV file (`flights_schedule.csv`) for future reference.
- **Visualization**: An interactive timeline chart is generated using Altair to visualize runway usage over time.

## How It Works

1. **Input Flight Details**: Users input the number of flights and provide details such as arrival time, departure time, flight type, and class for each flight.
2. **Schedule Flights**: Once all details are entered, users can click the "Schedule Flights" button to save the data and calculate the required number of runways.
3. **Runway Calculation**: The system calculates the minimum number of runways needed, considering the constraints for private and military flights.
4. **Visualization**: The system generates an interactive timeline chart showing runway usage over time.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aryana-27/airplane-runway-scheduling-system.git
   cd airplane-runway-scheduling-system
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages using pip:
   ```bash
   pip install streamlit pandas altair
   ```

3. **Run the Application**:
   Start the Streamlit application by running:
   ```bash
   streamlit run daa.py
   ```


## Usage

1. **Enter Flight Details**: Input the number of flights and provide the necessary details for each flight.
2. **Schedule Flights**: Click the "Schedule Flights" button to save the data and calculate the required number of runways.
3. **View Results**: The system will display the total number of runways needed and show an interactive timeline chart of runway usage.

## Example

Here’s an example of how to use the application:

1. Enter the number of flights (e.g., 3).
2. For each flight, input the arrival time, departure time, flight type, and class.
3. Click "Schedule Flights".
4. The system will display the total number of runways needed and show a timeline chart of runway usage.

## video of demo - 
https://github.com/user-attachments/assets/37e09fec-4006-439c-80e5-58311e93096c

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
---

Feel free to customize this README file to better suit your project's needs!
