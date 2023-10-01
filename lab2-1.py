class CardManager:
    def question(self):
        print("Відповідь на запитання про картку")

class DepositManager:
    def question(self):
        print("Відповідь на запитання про депозит")

class CreditManager:
    def question(self):
        print("Відповідь на запитання про кредит")

class Manager:
    def create_manager(self, request):
        if request == "картка":
            return CardManager()
        elif request == "депозит":
            return DepositManager()
        elif request == "кредит":
            return CreditManager()
        else:
            raise ValueError("Невідомий тип запиту")

request = input("Стосовно чого ви маєте запитання? (картка, кредит, депозит): ")
bank = Manager()
manager = bank.create_manager(request)
manager.question()