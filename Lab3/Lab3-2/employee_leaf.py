from employee_component import EmployeeComponent


class EmployeeLeaf(EmployeeComponent):
    def __init__(self, name):
        self.name = name

    def perform_action(self, action):
        if action == EmployeeComponent.FIRE:
            print(f"{self.name} has been fired.")
        elif action == EmployeeComponent.TRANSFER:
            print(f"{self.name} has been transferred.")
        elif action == EmployeeComponent.VACATION:
            print(f"{self.name} has been sent on vacation.")
        elif action == EmployeeComponent.BONUS:
            print(f"{self.name} has been awarded a bonus.")
        else:
            print(f"Action '{action}' for employee {self.name}")