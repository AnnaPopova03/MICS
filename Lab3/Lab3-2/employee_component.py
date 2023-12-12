from abc import ABC, abstractmethod


class EmployeeComponent(ABC):
    # class constants representing possible actions
    FIRE = "fire"
    TRANSFER = "transfer"
    VACATION = "vacation"
    BONUS = "bonus"

    @abstractmethod
    def perform_action(self, action):
        pass