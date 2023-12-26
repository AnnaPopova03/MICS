class Condition:
    def __init__(self, parameter, operator, value):
        self.parameter = parameter
        self.operator = operator
        self.value = value

    def check(self, weather_metrics):
        # Check if the condition is met based on the given operator and value
        parameter_value = getattr(weather_metrics, self.parameter, None)
        if parameter_value is not None:
            if self.operator == '>' and parameter_value > self.value:
                return True
            elif self.operator == '<' and parameter_value < self.value:
                return True
            elif self.operator == '==' and parameter_value == self.value:
                return True
        return False
