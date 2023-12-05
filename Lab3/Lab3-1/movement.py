class NewMovement:
    def move(self):
        pass

def choose_movement(place, adapters):
    for adapter in adapters:
        result = adapter.move()
        if place.lower() in result.lower():
            return result
    return None