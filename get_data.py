# Eszközök keresése
import broadlink

# Eszköz keresése
devices = broadlink.discover(discover_ip_address='192.168.0.255')

# Első eszköz hitelesítése
device = devices[0]
print(device)
device.auth()

# Hőmérséklet lekérdezése
data = device.get_full_status()


# Adatok formázása és kiírása
def format_data(data):
    print("=== Termosztát adatok ===\n")
    print(f"Szoba hőmérséklet: {data['room_temp']}°C")
    print(f"Beállított hőmérséklet (Thermostat): {data['thermostat_temp']}°C")
    print(f"Külső érzékelő hőmérséklete: {data['external_temp']}°C")
    print(f"Üzemmód: {'Fűtés' if data['active'] != 0 else 'Kikapcsolva'}")
    print(f"Áramellátás: {'Be' if data['poweron'] else 'Ki'}")
    print(f"Automata mód: {'Engedélyezett' if data['auto_mode'] > 0 else 'Letiltott'}")
    print(f"Idő: {data['hour']:02}:{data['min']:02}:{data['sec']:02}, A hét napja: {data['dayofweek']}\n")

    print("=== Hétköznapi beállítások ===")
    for i, setting in enumerate(data['weekday']):
        print(
            f"{i+1}. időszak: {setting['start_hour']:02}:{setting['start_minute']:02} - "
            f"{setting['temp']}°C"
        )

    print("\n=== Hétvégi beállítások ===")
    for i, setting in enumerate(data['weekend']):
        print(
            f"{i+1}. időszak: {setting['start_hour']:02}:{setting['start_minute']:02} - "
            f"{setting['temp']}°C"
        )

    print("\n=== Egyéb beállítások ===")
    print(f"Maximális hőmérséklet: {data['svh']}°C")
    print(f"Minimális hőmérséklet: {data['svl']}°C")
    print(f"Hőmérséklet különbség: {data['dif']}°C")
    print(f"Érzékelő mód: {data['sensor']}")
    print(f"Távoli zárolás: {'Aktív' if data['remote_lock'] else 'Inaktív'}")


# Adatok kiírása
format_data(data)
