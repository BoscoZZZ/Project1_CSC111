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
import class_player
import class_World


class Puzzle:
    """ A puzzle in our text adventure game world.

    Instance Attributes:
        - hint: A little bit of hint of the puzzle for players who are attempting to solve it

    Representation Invariants:
        -

    """

    def __init__(self, hint: str) -> None:
        """ Initialize a new puzzle
        """
        self.hint = hint
        self.solved = False


class CombineItem(Puzzle):
    """ Part of the puzzle that require players to combine items that will be needed.

    Instance Attributes:
        - hint: A little bit of hint of the puzzle for players who are attempting to solve it
        - required_material: the required material for players to combine
        - combined_item: the combined item

    Representation Invariants:
        -
    """

    def __init__(self, hint: str, required_material: str, combined_item: str) -> None:
        """ Initialize the item combination part of the puzzle
        """
        super().__init__(hint)
        self.hint = hint
        self.required_material = required_material
        self.combined_item = combined_item
        self.solved = False

    def combine_item(self, player: class_player.Player):
        """ Verify if players are eligible for combining items
        """
        if all(item in player.inventory for item in self.required_material):
            for item in self.required_material:
                player.inventory.remove(item)
            player.inventory.append(self.combined_item)
            self.solved = True
        return self.solved

    def hint_combine(self):
        """ Provide a hint for combining if player cannot solve
        """
        if not self.solved:
            print("What two things in your inventory can be combined to get a key?")


class OpenChest(Puzzle):
    """ Part of the puzzle that require players to use to the combined item to open the locked chest.

    Instance Attributes:
        - hint: A little bit of hint of the puzzle for players who are attempting to solve it
        - special_inventory:

    Representation Invariants:
        -
    """

    def __init__(self, hint: str, combined_item: str, final_item: str, chest_location: tuple) -> None:
        """ Initialize the use combined item to open the chest part of the puzzle
        """
        super().__init__(hint)
        self.hint = hint
        self.combined_item = combined_item
        self.final_item = final_item
        self.chest_location = chest_location
        self.solved = False

    def open_chest(self, player: class_player.Player, world: class_World.World):
        curr = world.get_location(player.x, player.y)
        chest_location = 2   # set to random number for now, have no idea what to set
        if curr == chest_location and self.combined_item in player.inventory:
            # not implement for now, if player is at the chest's location, "Open chest" option can be added
            # to the available action of players at that location
            player.inventory.append(self.final_item)
            self.solved = True
        return self.solved

    def chest_hint(self):
        """ Provide a hint for how to open the chest
        """
        if not self.solved:
            print("What item in your inventory can be used to open the chest?")
