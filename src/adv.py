from room import Room
from player import Player
import textwrap
from items import Item

# =================  Declare rooms  =========================

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# ===================== Link rooms together  ========================

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# ======================= Add items to rooms ========================

room['outside'].items.append(Item("rock", "It's a fist sized rock"))
room['outside'].items.append(Item("debris", "A pile of trash"))
room['foyer'].items.append(
    Item("orb", "A funny looking key with a skull on it"))
room['overlook'].items.append(
    Item("key", "A funny looking key with a skull on it"))

# print("This:")
# print(room['outside'].items[0].description)
# print(room['outside'].items[1])

# =========================  Main  ================================

# print(room['outside'].items)

player_name = input("What's your character's name?")
player = Player(player_name, room['outside'])
print(f"\nWelcome {player}\n")


while True:
    # * Prints the current description (the textwrap module might be useful here).
    print("------------------------------\n")
    print(player.current_room)
    print(f"You can go: {player.current_room.get_room_exits()}\n")
    print(f"You see:")
    for item in player.current_room.items:
        print(f" - {item}")
    cmd = input("\n=>")
    print("")

    if cmd == "q":   # If the user enters "q", quit the game.
        break

    elif cmd in ["n", "s", "e", "w"]:           # Directional commands
        player.travel(cmd)

    elif cmd.split(' ')[0] == "take":
        new_item = player.get_item(cmd.split(' ')[1])
        print(f"You picked up {new_item}\n")

    elif cmd == "inv":
        for item in player.items:
            print(f" - {item}")

    # If the user enters help, display a list actions that can be taken

    # Catch all message, command not available, please try again
    else:
        print("\nYou stand there stupidly.\n")
