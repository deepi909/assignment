def get_weather_info(weather_data, date_str, key):
    date = int(date_str)
    for data in weather_data.get("list", []):
        if date == data.get("dt"):
            return data.get(key, f"Data not available for date {date_str}")
    return f"Date not found in the hourly forecast."

def main():
    weather_data = {
        "cod": "200",
        "message": 0.0151,
        "cnt": 96,
        "list": [
            {
                "dt": 1553709600,
                "main": {
                    "temp": 278.76,
                    "temp_min": 278.76,
                    "temp_max": 279.558,
                    "pressure": 1031.934,
                    "humidity": 100,
                },
                "wind": {
                    "speed": 1.6,
                },
                "dt_txt": "2019-03-27 18:00:00"
            }
        ]
    }

    while True:
        print("\nSelect an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input()

        if choice == '0':
            print("Exiting...")
            break

        if choice in ['1', '2', '3']:
            date_str = input("Enter date (Unix timestamp): ")
            key = {"1": "main/temp", "2": "wind/speed", "3": "main/pressure"}.get(choice)
            result = get_weather_info(weather_data, date_str, key)
            print(f"Result: {result}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



