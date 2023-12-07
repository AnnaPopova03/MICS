from movement import NewMovement
from ski_movement import SkiMovement


class SkiAdapter(NewMovement):
    def __init__(self, ski_movement):
        self.ski_movement = ski_movement

    def move(self):
        return self.ski_movement.move_on_skis()