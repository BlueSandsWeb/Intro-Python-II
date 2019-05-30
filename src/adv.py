from room import Room
from player import Player
import textwrap
# from item import item

# =================  Declare rooms  =========================

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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


# =========================  Main  ================================


player_name = input("What's your character's name?")
player = Player(player_name, room['outside'])
print(f"\nWelcome {player}\n")


while True:
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room)
    cmd = input("\n=>")
    print("")

    if cmd == "q":   # If the user enters "q", quit the game.
        break

# If the user enters a cardinal direction, attempt to move to the room there.
    elif cmd in ["n", "s", "e", "w"]:
        player.travel(cmd)

    # If the user enters Spells, list spells and ask which to use
    # If the user enters help, display a list actions that can be taken

    # Catch all message, command not available, please try again
    else:
        print("\nYou stand there stupidly.\n")


"""
player = Player("Brady", room['outside'])
print(player.currentRoom)

rock = Item("rock", "This is a rock")
room['outside']

while True:
    cmd = input("-> ")
    if cmd in ["n", "s", "e", "w"]:
        player.travel(cmd)
    elif cmd == "q":
        break
    else:
        print("I did not understand that command\n")
"""
