"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import Optional, TextIO
import class_item


def quit_game():
    """ Game Over

    """
    print("Game Over")
    exit()


def move_tracker():
    command = input("Which direction do you want to go: ")
    if command in ["north", "south", "west", "east"]:
        Player.move_increment()


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - x: The player's x coordinates
        - y: The player's y coordinates
        - inventory: The player's inventory
        - victory: A boolean whether showing whether the player had won or not.

    Representation Invariants:
        - # TODO
    """

    def __init__(self, x: int, y: int, move_limit: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.move_limit = move_limit
        self.current_move = 0

    def pick_up_item(self, item: class_item.Item):
        """ Allow players to pick up items if they are at the item's location.

        """
        if (self.x, self.y) == item.start_position:
            self.inventory.append(item)
            item.current_position = None
            # Item's start position is unique, and the purpose of current location is that if the player dropped the
            # item, they will be dropped at the current location, where the player currently standing, and waiting to
            # be collect again if intended.
            item.pick_up_state = False
            return f"Wow! you discovered a {item.name}"
        elif (self.x, self.y) == item.current_position and item.pick_up_state:
            self.inventory.append(item)
            item.current_position = None
            item.pick_up_state = False
            return f"You picked up {item.name} again. (What you dropped before)"

    def drop_item(self, item: class_item.Item):
        """ Allow players to drop items in their inventory anytime they want.

        """
        if item in self.inventory:
            self.inventory.remove(item)
            item.current_position = (self.x, self.y)
            return f"You successfully dropped {item.name} here!"
        else:
            return f"{item.name} is not in your inventory."

    def inventory(self):
        """ Allow players to get items

        """
        if not self.inventory:
            return "Your inventory is empty"
        else:
            inventory_list = [item.name for item in self.inventory]

        return inventory_list

    def move_increment(self):
        self.current_move += 1
        if self.current_move >= self.move_limit:
            quit_game()

