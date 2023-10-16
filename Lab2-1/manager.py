from cardManager import CardManager
from depositManager import DepositManager
from creditManager import CreditManager

class Manager:
    card = "card" #constant
    deposit = "deposit" #constant
    credit = "credit" #constant

    def create_manager(self, request):
        if request == self.card:
            return CardManager()
        elif request == self.deposit:
            return DepositManager()
        elif request == self.credit:
            return CreditManager()
        else:
            raise ValueError("Unknown request")
