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


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """

    def __init__(self, name: str, loc_number: int, loc_item: Item, brief_desc: str, long_desc: str) -> None:
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
        # self.loc_item = loc_item
        self.brief_desc = brief_desc
        self.long_desc = long_desc

    def available_actions(self):
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """

        # NOTE: This is just a suggested method
        # i.e. You may remove/modify/rename this as you like, and complete the
        # function header (e.g. add in parameters, complete the type contract) as needed

        # TODO: Complete this method, if you'd like or remove/replace it if you're not using it


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """

    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
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


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """

    def __init__(self, x: int, y: int) -> None:
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


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - # TODO add more instance attributes as needed; do NOT remove the map attribute

    Representation Invariants:
        - # TODO
    """

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)
        self.location_data = self.load_location(location_data)
        self.items_data = self.load_items(items_data)

        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        # TODO: DONE: UNCHECKED Complete this method as specified. Do not modify any of this function's specifications.
        self.map = []
        # create a new map list storing data
        for line in map_data:
            # traversing map_data and put them in self.map line by line
            self.map.append([int(num) for num in line.split()])

        return self.map

    # TODO: Add methods for loading location data and item data (see note above).
    def load_location(self, locations_data: TextIO) -> list[Optional[Location]]:
        """
        Store location from open file locations.data as the location attribute of this object

        If locations_data is a file containing the following text:

        LOCATION Robarts Library
        3
        You are outside the Robarts library.
        You are outside the Robarts library on a crowded street. There is a smell of coffee in the air.
        END

        load_location should assign this World object's lcoation to store in the class location in the following format
        self.name = 'LOCATION Robarts Library'
        self.loc_number = 3
        self.brief_desc = 'You are outside the Robarts library.'
        self.long_desc = 'You are outside the Robarts library ...'
        it will start to store next location when END is found

        Return this list representation of the location.
        """
        self.locations = []
        lines = locations_data.readlines()
        i = 0
        while i < len(lines):
            if lines[i].startswith("LOCATION"):
                self.name = lines[i].strip()
                self.loc_number = int(lines[i + 1])
                self.brief_desc = lines[i + 2].strip()
                self.long_desc = ""
                j = i + 3
                while j < len(lines) and not lines[j].startswith("END"):
                    self.long_desc += lines[j]
                    j += 1
                self.locations.append(Location(self.name, self.loc_number, self.brief_desc, self.long_desc))
                i = 0
            else:
                i += 1
        return self.locations

    def load_items(self, items_data: TextIO) -> list[Optional[Item]]:
        """
        Store items from open file items_data as the item attribute of this object, as a nested list of integers like so:

        If item_data is a file containing the following text:
            1 10 5 Cheat Sheet
        then item under self where it can be names since it is store in an item

        Return this list of items
        """
        self.items = []
        # create a new items list to store data
        for line in items_data:
            # traversing the text file and store base on every line
            fields = line.split()
            item = Item(fields[3], int(fields[0]), int(fields[1]), int(fields[2]))
            # fields[3] represent the last variable which is name, this will be store in self.name
            # the rest are similar as above fields[3]
            self.items.append(item)
            # append

        return self.items

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        # TODO: DONE: UNCHECKED Complete this method as specified. Do not modify any of this function's specifications.
        if x < 0 or y < 0 or x >= len(self.map) or y >= len(self.map[0]):
            # This is the case where one of them is out of bound
            return None
        elif self.map[x][y] == -1:
            # This is the case where the number is -1 on the map
            return None
        else:
            # Return the location
            return Location(self.map[x][y])
