import os
from price_list import PriceList
from service import Service


SUMMER_SEASON = "summer"
WINTER_SEASON = "winter"
FILENAME = "pricelist.txt"

def input_service():
    name = input("Enter name of service: ")
    price = float(input("Enter price: "))
    return Service(name, price)

def save_to_file(pricelist, FILENAME):
    with open(FILENAME, 'w') as file:
        file.write(f"{SUMMER_SEASON}:\n")
        for service in pricelist.summer:
            file.write(f"{service.name} - {service.price} grn\n")
        file.write(f"{WINTER_SEASON}:\n")
        for service in pricelist.winter:
            file.write(f"{service.name} - {service.price} grn\n")

def load_from_file(filename):
    pricelist = PriceList()
    current_season = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line == f"{SUMMER_SEASON}:":
                current_season = SUMMER_SEASON
            elif line == f"{WINTER_SEASON}:":
                current_season = WINTER_SEASON
            elif current_season and line:
                name, price_str = line.split(" - ")
                price = float(price_str.replace(" grn", ""))
                service = Service(name, price)
                if current_season == SUMMER_SEASON:
                    pricelist.add_summer_service(service)
                elif current_season == WINTER_SEASON:
                    pricelist.add_winter_service(service)
    return pricelist

def main():
    try:
        pricelist = load_from_file(FILENAME)
    except FileNotFoundError:
        pricelist = PriceList()

    while True:
        print("\nMenu:")
        print("1) Add service")
        print("2) View price list")
        print("3) Exit")
        
        ch = input("Select an action (1/2/3): ")
        if ch == "1":
            new_service = input_service()
            season = input("Select season (summer or winter): ")
            if season == SUMMER_SEASON:
                pricelist.add_summer_service(new_service)
            elif season == WINTER_SEASON:
                pricelist.add_winter_service(new_service)
            save_to_file(pricelist, FILENAME)
            print("The service is added successfully")
        elif ch == "2":
            season = input("Select season (summer or winter): ")
            services = pricelist.get_services(season)
            if services:
                print(f"{season} services:")
                for service in services:
                    print(service)
            else:
                print(f"Services for the {season} season were not found.")
        elif ch == "3":
            print("Exit")
            break
        else:
            print("Incorrect data. Try again")

if __name__ == "__main__":
    main()
