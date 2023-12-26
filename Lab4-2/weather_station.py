import random
from weather_metrics import WeatherMetrics
from observer import Observer
from observable import Observable


class WeatherStation(Observable):
    def __init__(self):
        self.observers = []  # List to store subscribed observers
        self.weather_metrics = WeatherMetrics(0, 0, 0, "", 0)  # Initial weather metrics

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, weather_metrics):
        for observer in self.observers:
            observer.update(weather_metrics)

    def add_threshold_observer(self, observer, conditions):
        observer.set_conditions(conditions)
        self.add_observer(observer)

    def set_weather_metrics(self, new_metrics):
        self.weather_metrics = new_metrics
        self.notify_observers(new_metrics)

    def simulate_weather_change(self):
        # Simulate random weather change
        new_temperature = random.randint(-10, 30)
        new_humidity = random.randint(0, 100)
        new_wind_speed = random.randint(0, 20)
        new_wind_direction = random.choice(['N', 'S', 'W', 'E'])
        new_pressure = random.randint(980, 1030)

        new_weather_metrics = WeatherMetrics(new_temperature, new_humidity, new_wind_speed, new_wind_direction, new_pressure)
        self.set_weather_metrics(new_weather_metrics)