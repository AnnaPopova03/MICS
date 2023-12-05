from adapter import BoatAdapter, HangGliderAdapter, SkiAdapter
from boat_movement import BoatMovement
from hang_glider_movement import HangGliderMovement
from ski_movement import SkiMovement
from movement import choose_movement


places = ["river", "gorge", "snow"] 

boat_adapter = BoatAdapter(BoatMovement())
hang_glider_adapter = HangGliderAdapter(HangGliderMovement())
ski_adapter = SkiAdapter(SkiMovement())

print("Select a location:")
for i, place in enumerate(places, 1):
    print(f"{i}. {place}")

ch = int(input("Enter number: "))

if 1 <= ch <= len(places):
    chosen_place = places[ch - 1]
    result = choose_movement(chosen_place, [boat_adapter, hang_glider_adapter, ski_adapter])
    if result:
        print(f"You can suit {result}.")
else:
    print("Incorrect choice")
