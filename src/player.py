# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.hp = 15
        self.mp = 15
        self.spells = [
            {'name': 'fireball', 'cost': 2, 'damage': 3},
            {'name': 'spark', 'cost': 1, 'damage': 2}
        ]

    def __str__(self):
        return (f"{self.name}")

    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            # print(self.current_room)
        else:
            print("You can't go that way.\n")

    def list_spells(self):
        print(f"Here's a list of your spells\n")
        for spell in (self.spells):
            print(
                f"{spell['name']}, cost: {spell['cost']}, damage: {spell['damage']}")
        print()


"""

class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(self.currentRoom)
        else:
            print("You cannot move in that direction.")

"""
