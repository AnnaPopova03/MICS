from boat_adapter import BoatAdapter
from hang_glider_adapter import HangGliderAdapter
from ski_adapter import SkiAdapter
from boat_movement import BoatMovement
from hang_glider_movement import HangGliderMovement
from ski_movement import SkiMovement
from movement import choose_movement


places = ["river", "gorge", "snow"] # list of available locations

# create instances of adapters for different movement types
boat_adapter = BoatAdapter(BoatMovement())
hang_glider_adapter = HangGliderAdapter(HangGliderMovement())
ski_adapter = SkiAdapter(SkiMovement())

print("Select a location:") # display the available locations for the user to choose from
for i, place in enumerate(places, 1):
    print(f"{i}. {place}")
    
ch = int(input("Enter number: ")) # prompt the user to enter a number corresponding to their chosen location

if 1 <= ch <= len(places): # check if the user's choice is within the valid range
    chosen_place = places[ch - 1]
    # use the function to find a suitable movement for the chosen location
    result = choose_movement(chosen_place, [boat_adapter, hang_glider_adapter, ski_adapter])
    if result: # if a suitable movement is found
        print(f"You can use {result}.")
else:
    print("Incorrect choice") # error message for an incorrect choice
