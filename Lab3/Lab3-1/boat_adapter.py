from movement import NewMovement
from boat_movement import BoatMovement


class BoatAdapter(NewMovement):
    def __init__(self, boat_movement):
        self.boat_movement = boat_movement

    def move(self):
        return self.boat_movement.move_on_boat()