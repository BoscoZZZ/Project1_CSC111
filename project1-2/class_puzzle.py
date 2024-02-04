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

    def __init__(self, hint: str, required_material: list[str], combined_item: str) -> None:
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
            print(self.hint)


class OpenChest(Puzzle):
    """ Part of the puzzle that require players to use to the combined item to open the locked chest.

    Instance Attributes:
        - hint: A little bit of hint of the puzzle for players who are attempting to solve it
        - special_inventory:

    Representation Invariants:
        -
    """

    def __init__(self, hint: str, combined_item: str, final_item: str, chest_location: int) -> None:
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
        if curr == self.chest_location and self.combined_item in player.inventory:
            player.inventory.append(self.final_item)
            self.solved = True
        return self.solved

    def chest_hint(self):
        """ Provide a hint for how to open the chest
        """
        if not self.solved:
            print(self.hint)


class MissileLaunch(Puzzle):
    """ Another puzzle that requires players to use the missile launch pad and password to destroy
    a place called super castle and get the things they needed to win the game.

    Instance Attributes:
        - hint: A little bit of hint of the puzzle for players who are attempting to solve it
        -

    Representation Invariants:
        -

    """

    def __init__(self, hint: str, password: int, launch_pad: str, sealed_item: str, target_loc: str):
        super().__init__(hint)
        self.password = password
        self.launch_pad = launch_pad
        self.sealed_item = sealed_item
        self.target_loc = target_loc
        self.solved = False

    def check_password(self, player_input: int):
        """ Check if players input the correct password
        """
        return player_input == self.password

    def use_launch_pad(self, player: class_player.Player, player_input: int, world:class_World.World):
        """ Launch the missile if players discovered the launch as well as input the correct the password
        """
        if self.check_password(player_input) and self.launch_pad in player.inventory:
            target_loc = world.locations[self.target_loc]
            world.destroy_location(target_loc)
            player.inventory.append(self.sealed_item)
            self.solved = True
        return self.solved

    def missile_hint(self):
        if not self.solved:
            print(self.hint)


class BusinessmanTrading(Puzzle):
    """ Part of the puzzle that players need to trade an item with a businessman to get the item they need

    Instance Attributes:
        - hint: A little bit of hint of the puzzle for players who are attempting to solve it
        - exchange_item: item that players exchange with the businessman
        - crucial_item: a list of special items that if players trade them will result in losing the game directly

    Representation Invariants:
        -

    """

    def __init__(self, hint: str, exchange_item: str, crucial_item: list[str], business_location: int):
        super().__init__(hint)
        self.exchange_item = exchange_item
        self.crucial_item = crucial_item
        self.business_location = business_location
        self.traded_or_not = False

    def trade(self, player: class_player.Player, item_to_trade):
        """ Notice that if you give the businessman something you need in order to win the game, you lose the game
        directly! So be careful with what you choose to trade, the businessman is going to give you something you need!
        Notice that you can only trade with him once, once you trade with him successfully, and you go back to the same
        location, you won't be able to trade with him again! However, if you didn't trade with him upon first visit, you
        can still trade with him later.

        """
        if self.traded_or_not:
            print("You already trade with me comrade! I have nothing left to give you.")
        if item_to_trade in self.crucial_item:
            print("Oh, you trade this precious thing with me! You won't be able to attend your test! HAHA!")
            player.victory = False
        else:
            player.inventory.remove(item_to_trade)
            player.inventory.append(self.exchange_item)
            self.traded_or_not = True


def available_action(player: class_player.Player, item: CombineItem, world: class_World.World,
                     chest: OpenChest, missile: MissileLaunch, business: BusinessmanTrading):
    """ Return a list of special available action
    """
    actions = []
    if all(item in player.inventory for item in item.required_material):
        actions.append("combine")
    curr = world.get_location(player.x, player.y)
    if curr == chest.chest_location and chest.combined_item in player.inventory:
        actions.append("open_chest")
    if missile.launch_pad in player.inventory:
        actions.append("type_password")
    if not business.traded_or_not and curr == business.business_location:
        actions.append("trade")
    return actions
