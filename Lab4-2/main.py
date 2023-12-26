from weather_station import WeatherStation
from user import User
from condition import Condition


def main():
    parameter_mapping = { # Mapping for user-friendly parameter labels
        't': 'temperature',
        'h': 'humidity',
        'ws': 'wind_speed',
        'wd': 'wind_direction',
        'p': 'pressure',
    }

    weather_station = WeatherStation()

    while True:
        print("\n1. Show Weather / Simulate Weather Change")
        print("2. Add Subscriber with Condition")
        print("3. Exit")

        ch = input("Select an option: ")

        if ch == '1':
            print("Simulating weather change...")
            weather_station.simulate_weather_change()
            weather_metrics = weather_station.weather_metrics
            print(f"Current weather metrics: {weather_metrics.__dict__}")

        elif ch == '2':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            user = User(name, email)
            conditions = []
            while True:
                param_input = input("Parameter (t/h/ws/wd/p): ").lower()
                if param_input not in parameter_mapping:
                    print("Invalid parameter label. Please try again.")
                    continue

                parameter = parameter_mapping[param_input]
                value = input("Value: ")

                if parameter == 'wind_direction' and value not in ['N', 'S', 'W', 'E']:
                    print("Invalid value for wind direction. Enter N, S, W, or E.")
                    continue

                try:
                    value = int(value)
                except ValueError:
                    pass

                operator = input("Operator (> or < or ==): ")
                condition = Condition(parameter, operator, value)
                conditions.append(condition)

                add_more = input("Add another condition? (yes/no): ")
                if add_more.lower() != 'yes':
                    break

            weather_station.add_threshold_observer(user, conditions)
            print(f"Subscriber {user.name} ({user.email}) added with conditions.")

        elif ch == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()