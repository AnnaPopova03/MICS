from abc import ABC, abstractmethod
from employee_component import EmployeeComponent


class DepartmentComposite(EmployeeComponent):
    def __init__(self, name):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def perform_action(self, action):
        if action == EmployeeComponent.FIRE:
            print(f"All employees in department {self.name} have been fired.")
        elif action == EmployeeComponent.TRANSFER:
            print(f"All employees in department {self.name} have been transferred.")
        elif action == EmployeeComponent.VACATION:
            print(f"All employees in department {self.name} have been sent on vacation.")
        elif action == EmployeeComponent.BONUS:
            print(f"All employees in department {self.name} have been awarded a bonus.")
        else:
            print(f"Action '{action}' for department {self.name}")

        for subordinate in self.subordinates:
            subordinate.perform_action(action)
