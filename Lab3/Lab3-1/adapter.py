from movement import NewMovement
from boat_movement import BoatMovement
from hang_glider_movement import HangGliderMovement
from ski_movement import SkiMovement


class BoatAdapter(NewMovement):
    def __init__(self, boat_movement):
        self.boat_movement = boat_movement

    def move(self):
        return self.boat_movement.move_on_boat()

class HangGliderAdapter(NewMovement):
    def __init__(self, hang_glider_movement):
        self.hang_glider_movement = hang_glider_movement

    def move(self):
        return self.hang_glider_movement.move_with_hang_glider()

class SkiAdapter(NewMovement):
    def __init__(self, ski_movement):
        self.ski_movement = ski_movement

    def move(self):
        return self.ski_movement.move_on_skis()
