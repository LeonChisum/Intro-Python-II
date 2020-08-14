from room import Room
from player import Player
from item import Item

# Declare all the rooms

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].items.append(Item("Car", "Fast use for transportation"))
room['foyer'].items.append(Item("Painting", "Visually pleasing representation of art"))
room['narrow'].items.append(Item("Rug", "Quality fabric made to make the feet feel like royalty"))
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Johnny', room['outside'])

# Write a loop that:
while True:

# * Prints the current room name
    print(f"Hello {player1.name} {player1.current_room.room_name()} ")


# * Prints the current description (the textwrap module might be useful here).
    print(f"{player1.current_room.description}")
# Items currently in the room
    print("These are the items that are currently in your room:")
    for item in player1.current_room.items:
        print(f"{item.name}: {item.description}")
# * Waits for user input and decides what to do.
    user_input = input("Pick a direction to move to the next room (ex. e , s , n, w?)")
# If the user enters a cardinal direction, attempt to move to the room there.
    inputs = ["n", "s", "e", "w"]
    if user_input == "q":
        break
    split = user_input.split()
    print(f"{split}")
    if len(split) == 1:
        attr = f"{user_input}_to"
        if hasattr(player1.current_room, attr):
            new_room = getattr(player1.current_room, attr)
            print(f"Hmmm, I see you are trying to move to {new_room.name}")
            player1.current_room = new_room
        else:
            print("That was not a valid direction to move")
            continue

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
