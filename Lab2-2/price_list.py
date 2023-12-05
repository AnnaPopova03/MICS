from service import Service


class PriceList:
    def __init__(self):
        self.summer = []
        self.winter = []
        
    def add_summer_service(self, service):
        self.summer.append(service)
        
    def add_winter_service(self, service):
        self.winter.append(service)
        
    def get_services(self, season):
        if season == "summer":
            return [service.clone() for service in self.summer]
        elif season == "winter":
            return [service.clone() for service in self.winter]
        else:
            return []
