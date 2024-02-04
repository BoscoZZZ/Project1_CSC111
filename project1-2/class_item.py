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


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name: The name of the item
        - start_position: The initial coordinates of the item
        - target_position: The coordinates where the item need to be deposited
        - target_points: The number of points awarded for depositing the item at target position
        - current_position: After players first discovered the item at the start_position, if they want to
                            drop the item. The new location of the item will be the current_position
        - pick_up_state: Indicate whether the item can be picked up or not at the moment

    Representation Invariants:
        - target_points >= 0
    """

    def __init__(self, name: str, start: int, target: int, target_points: int, curr: int, ) -> None:
        """Initialize a new item.
        """

        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points
        self.current_position = curr
        # determine if this item can be picked up

        self.pick_up_state = True


class PuzzleItem(Item):
    def __init__(self, name: str, start: int, target: int, target_points: int, curr: int, hint: str, puzzle_type: str):
        super().__init__(name, start, target, target_points, curr)
        self.hint = hint
        self.puzzle_type = puzzle_type
