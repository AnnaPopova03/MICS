from movement import NewMovement
from hang_glider_movement import HangGliderMovement


class HangGliderAdapter(NewMovement):
    def __init__(self, hang_glider_movement):
        self.hang_glider_movement = hang_glider_movement

    def move(self):
        return self.hang_glider_movement.move_with_hang_glider()