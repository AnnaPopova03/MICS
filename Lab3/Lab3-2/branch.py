from abc import ABC, abstractmethod
from employee import EmployeeComponent


class BranchComposite(EmployeeComponent):
    def __init__(self, name):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def perform_action(self, action):
        if action == "fire":
            print(f"All employees in branch {self.name} have been fired.")
        elif action == "transfer":
            print(f"All employees in branch {self.name} have been transferred.")
        elif action == "vacation":
            print(f"All employees in branch {self.name} have been sent on vacation.")
        elif action == "bonus":
            print(f"All employees in branch {self.name} have been awarded a bonus.")
        else:
            print(f"Action '{action}' for branch {self.name}")

        for subordinate in self.subordinates:
            subordinate.perform_action(action)
