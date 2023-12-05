from abc import ABC, abstractmethod


class EmployeeComponent(ABC):
    @abstractmethod
    def perform_action(self, action):
        pass

class EmployeeLeaf(EmployeeComponent):
    def __init__(self, name):
        self.name = name

    def perform_action(self, action):
        if action == "fire":
            print(f"{self.name} has been fired.")
        elif action == "transfer":
            print(f"{self.name} has been transferred.")
        elif action == "vacation":
            print(f"{self.name} has been sent on vacation.")
        elif action == "bonus":
            print(f"{self.name} has been awarded a bonus.")
        else:
            print(f"Action '{action}' for employee {self.name}")
