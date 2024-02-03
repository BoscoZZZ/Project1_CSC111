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
# from typing import Optional, TextIO
import class_item


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """

    def __init__(self, name: str, loc_number: int, loc_item: class_item.Item, brief_desc: str, long_desc: str) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
        """

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

        # TODO: Complete this method
        self.name = name
        self.loc_number = loc_number
        self.loc_item = loc_item
        self.brief_desc = brief_desc
        self.long_desc = long_desc
        self.visited = False
    #
    # def available_actions(self):
    #     """
    #     Return the available actions in this location.
    #     The actions should depend on the items available in the location
    #     and the x,y position of this location on the world map.
    #     """
    #
    #     # NOTE: This is just a suggested method
    #     # i.e. You may remove/modify/rename this as you like, and complete the
    #     # function header (e.g. add in parameters, complete the type contract) as needed
    #
    #     # TODO: Complete this method, if you'd like or remove/replace it if you're not using it

    def get_full_description(self):
        """ Return the full description of the location upon first visit

        """
        return f"LOCATION {self.loc_number}\n\n{self.long_desc}"

    def get_brief_description(self):
        """ Return a brief description of the location if not player's first visit

        """
        return f"LOCATION {self.loc_number}\n\n{self.brief_desc}"

    def available_actions(self):
        """
        Return a list of available actions at this location.
        """
        actions = []
        if self.loc_item and self.loc_item.pick_up_state:
            actions.append(f"Pick up {self.loc_item.name}")

        # Additional actions based on location-specific logic can be added here

        return actions
