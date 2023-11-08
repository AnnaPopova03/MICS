from cardManager import CardManager
from depositManager import DepositManager
from creditManager import CreditManager

class Manager:
    CARD = "card" 
    DEPOSIT = "deposit" 
    CREDIT = "credit"

    managers = {
        CARD: CardManager(),
        DEPOSIT: DepositManager(),
        CREDIT: CreditManager()
    }

    def create_manager(self, request):
        if request in self.managers:
            return self.managers[request]
        else:
            raise ValueError("Unknown request")
