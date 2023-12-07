class NewMovement:
    def move(self):
        pass

def choose_movement(place, adapters):
    for adapter in adapters: # iterate through the list of adapters
        result = adapter.move()  # call the move() method of each adapter
        if place.lower() in result.lower(): # check if the specified place is mentioned in the result
            return result # if the place is found
    return None # if no matching place is found in any adapter's result
