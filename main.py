# Device discovery
import broadlink

# Discover devices
devices = broadlink.discover(discover_ip_address='192.168.1.255')

# Authenticate the first device
device = devices[0]
print(device)
device.auth()

# Retrieve temperature data
data = device.get_full_status()

# Format and display data
def format_data(data):
    print("=== Thermostat Data ===\n")
    print(f"Room Temperature: {data['room_temp']}°C")
    print(f"Set Temperature (Thermostat): {data['thermostat_temp']}°C")
    print(f"External Sensor Temperature: {data['external_temp']}°C")
    print(f"Mode: {'Heating' if data['active'] != 0 else 'Off'}")
    print(f"Power: {'On' if data['poweron'] else 'Off'}")
    print(f"Auto Mode: {'Enabled' if data['auto_mode'] > 0 else 'Disabled'}")
    print(f"Time: {data['hour']:02}:{data['min']:02}:{data['sec']:02}, Day of the Week: {data['dayofweek']}\n")

    print("=== Weekday Settings ===")
    for i, setting in enumerate(data['weekday']):
        print(
            f"{i+1}. Period: {setting['start_hour']:02}:{setting['start_minute']:02} - "
            f"{setting['temp']}°C"
        )

    print("\n=== Weekend Settings ===")
    for i, setting in enumerate(data['weekend']):
        print(
            f"{i+1}. Period: {setting['start_hour']:02}:{setting['start_minute']:02} - "
            f"{setting['temp']}°C"
        )

    print("\n=== Other Settings ===")
    print(f"Maximum Temperature: {data['svh']}°C")
    print(f"Minimum Temperature: {data['svl']}°C")
    print(f"Temperature Difference: {data['dif']}°C")
    print(f"Sensor Mode: {data['sensor']}")
    print(f"Remote Lock: {'Active' if data['remote_lock'] else 'Inactive'}")

# Display data
format_data(data)