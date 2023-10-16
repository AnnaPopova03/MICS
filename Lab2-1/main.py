from manager import Manager

request = input("What do you have a question about? (card, deposit, credit): ") #user data input
bank = Manager()
manager = bank.create_manager(request) #creating a manager of the required type
manager.question() #contact the manager
