# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = list[Item] = []

    def room_name(self):
        print(f"You are currently located in {self.name}")