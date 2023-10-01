import copy

class ServicePrototype:
    def clone(self):
        return copy.deepcopy(self)

class Service(ServicePrototype):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} - {self.price} грн"

class PriceList:
    def __init__(self):
        self.summer = []
        self.winter = []
    def add_summer_service(self, service):
        self.summer.append(service)
    def add_winter_service(self, service):
        self.winter.append(service)
    def get_services(self, season):
        if season == "літо":
            return [service.clone() for service in self.summer]
        elif season == "зима":
            return [service.clone() for service in self.winter]
        else:
            return []

def input_service():
    name = input("Введіть назву послуги: ")
    price = float(input("Введіть ціну послуги: "))
    return Service(name, price)

def save_to_file(pricelist, filename):
    with open(filename, 'w') as file:
        file.write("літо:\n")
        for service in pricelist.summer:
            file.write(f"{service.name} - {service.price} грн\n")
        file.write("зима:\n")
        for service in pricelist.winter:
            file.write(f"{service.name} - {service.price} грн\n")

def load_from_file(filename):
    pricelist = PriceList()
    current_season = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "літо:":
                current_season = "літо"
            elif line == "зима:":
                current_season = "зима"
            elif current_season and line:
                name, price_str = line.split(" - ")
                price = float(price_str.replace(" грн", ""))
                service = Service(name, price)
                if current_season == "літо":
                    pricelist.add_summer_service(service)
                elif current_season == "зима":
                    pricelist.add_winter_service(service)
    return pricelist

filename = "pricelist.txt"
try:
    pricelist = load_from_file(filename)
except FileNotFoundError:
    pricelist = PriceList()

while True:
    print("\nМеню:")
    print("1) Додати послугу")
    print("2) Переглянути прайс-лист")
    print("3) Вихід")
    
    ch = input("Оберіть дію (1/2/3): ")
    if ch == "1":
        new_service = input_service()
        season = input("Укажіть сезон послуги (літо чи зима): ")
        if season == "літо":
            pricelist.add_summer_service(new_service)
        elif season == "зима":
            pricelist.add_winter_service(new_service)
        save_to_file(pricelist, filename)
        print("Послугу додано успішно")
    elif ch == "2":
        season = input("Введіть сезон (літо или зима): ")
        services = pricelist.get_services(season)
        if services:
            print(f"Послуги для сезону {season}:")
            for service in services:
                print(service)
        else:
            print(f"Послуг для сезону {season} не знайдено.")
    elif ch == "3":
        print("Вихід")
        break
    else:
        print("Некоректні дані. Спробуйте знову")