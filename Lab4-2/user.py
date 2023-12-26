from observer import Observer


class User(Observer):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.conditions = []  # List to store user-defined conditions

    def add_condition(self, condition):
        self.conditions.append(condition)

    def set_conditions(self, conditions):
        self.conditions = conditions

    def update(self, weather_metrics):
        updated_metrics = {k: v for k, v in weather_metrics.__dict__.items()}
        for condition in self.conditions:
            if condition.check(weather_metrics):
                print(f"User {self.name} ({self.email}) received weather update: {updated_metrics}")
