# Broadlink Thermostat Data Fetcher

This Python script is designed to retrieve and display data from thermostats equipped with Hysen HY02/HY03 chips, such as the Computherm E400RF thermostat. It connects to the thermostat via the local network, authenticates it, and retrieves various parameters like room temperature, target temperature, and scheduling settings.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/montpiere/HysenThermostatMonitor.git
   cd broadlink-thermostat
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the script, ensure that the IP address provided in `discover_ip_address` matches your network's IP range. For example:
   
   - If your local network uses the `192.168.1.x` range, set `discover_ip_address='192.168.1.255'`.
   - If your network uses `192.168.0.x`, change it to `discover_ip_address='192.168.0.255'`.
   
This setting ensures the script correctly discovers the thermostat on your network.

## Usage

Run the script with the following command:
   ```bash
   python main.py
   ```

The script will:
- Discover the thermostat on the network.
- Authenticate the device.
- Retrieve and display temperature data and settings.

## Settings and Features
- **Room Temperature:** Displays the current temperature measured by the thermostat.
- **Set Temperature:** Shows the user-defined target temperature.
- **External Sensor Temperature:** If applicable, retrieves data from an external sensor.
- **Operating Mode:** Indicates whether heating is active or off.
- **Power Status:** Displays whether the thermostat is powered on or off.
- **Auto Mode:** Shows if automatic scheduling is enabled.
- **Time & Day of the Week:** Retrieves and displays the current time and weekday settings.
- **Weekday & Weekend Scheduling:** Lists programmed temperature periods.
- **Advanced Settings:** Includes maximum/minimum temperature limits, sensor mode, and remote lock status.
