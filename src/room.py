# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        return (f"{self.name}: {self.description}\n")

    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def get_room_exits(self):
        exits = []
        if self.n_to != None:
            exits.append("n")
        if self.s_to != None:
            exits.append("s")
        if self.e_to != None:
            exits.append("e")
        if self.w_to != None:
            exits.append("w")
        if len(exits) == 0:
            return "You're trapped!"
        return exits
