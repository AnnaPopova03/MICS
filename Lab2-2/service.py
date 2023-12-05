from service_prototype import ServicePrototype


class Service(ServicePrototype):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"{self.name} - {self.price} grn"
