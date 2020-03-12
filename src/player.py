# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Food
class Player:
    def __init__(self, name, current_room,):
        self.name = name
        self.current_room = current_room
        self.items = []
    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print("you cannot move in that direction")
    def print_inventory(self):
        print("Your inventory: ")
        for item in self.items:
            print(item.name)
    def eat(self, food_item):
        if not isinstance(food_item, Food):
            print("That's not food!")
        else:
            print(f"You eat {food_item.name}")
            self.items.remove(food_item)