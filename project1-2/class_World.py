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
import class_location
import class_item
import class_player


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - location_data: a nested list of location object of the world
        - items_data: a newsted list of item object of the world
        - locations: initial empty world if not text read
        - items: initial empty items if not item read

    Representation Invariants:
        - # TODO
    """

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """
        self.world_map = self.load_map(open("map.txt"))
        self.adv_location = self.load_location(open("locations.txt"))

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
        self.locations = []
        self.items = []

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
    def load_location(self, locations_data: TextIO) -> list[Optional[class_location.Location]]:
        """
        Store location from open file locations data as the location attribute of this object

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
        item_instance = class_item.Item("", -2, -2, -2, -2)
        self.locations = []
        lines = locations_data.readlines()
        i = 0
        while i < len(lines):
            if lines[i].startswith("LOCATION"):
                name = lines[i].strip()
                loc_number = int(lines[i + 1])
                brief_desc = lines[i + 2].strip()
                long_desc = ""
                j = i + 3
                while j < len(lines) and not lines[j].startswith("END"):
                    long_desc += lines[j]
                    j += 1
                location = class_location.Location(name, loc_number, item_instance, brief_desc,
                                                   long_desc)  # Assuming None for loc_item
                self.locations.append(location)
                i = j  # Move to the line after "END"
            else:
                i += 1
        return self.locations

    def load_items(self, items_data: TextIO) -> list[Optional[class_item.Item]]:
        """
        Store items from open file items_data as the item attribute of this object,
        as a nested list of integers like so:

        If item_data is a file containing the following text:
            1 10 5 Cheat Sheet
        then item under self where it can be names since it is store in an item

        Return this list of items
        """
        self.items = []
        for line in items_data:
            fields = line.split()
            if fields[0] == "hint":
                # Assuming the PuzzleItem class constructor matches these parameters
                item = class_item.PuzzleItem(fields[5], int(fields[2]), int(fields[3]), int(fields[4]), int(fields[2]),
                                             fields[1], fields[6])
            else:
                # Assuming the Item class constructor matches these parameters
                item = class_item.Item(fields[3], int(fields[0]), int(fields[1]), int(fields[2]), int(fields[0]))
            self.items.append(item)
        return self.items
        # self.items = []
        # # create a new items list to store data
        # for line in items_data:
        #     fields = line.split()
        #     if fields[0] == "hint":
        #         item.hint = fields[1]
        #         item.start_position = int(fields[2])
        #         item.target_position = int(fields[3])
        #         item.target_points = int(fields[4])
        #         item.name = fields[5]
        #         item.puzzle_type = fields[6]
        #         item = class_item.PuzzleItem(item.name, item.start_position, item.target_position, item.target_points,
        #                                      item.start_position, item.hint, item.puzzle_type)
        #     else:
        #         item.name = fields[3].lower()
        #         item.start_position = int(fields[0])
        #         item.target_position = int(fields[1])
        #         item.target_points = int(fields[2])
        #         item.current_position = int(fields[0])
        #         item = class_item.Item(item.name, item.start_position, item.target_position, item.target_points,
        #                                item.current_position)
        #     self.items.append(item)
        # return self.items

        #     # traversing the text file and store base on every line
        #     fields = line.split()
        #     item = class_item.Item(fields[3].lower(), int(fields[0]), int(fields[1]), int(fields[2]),
        #                            int(fields[0]), '', '')
        #     puzzle_item = class_item.Item(fields[4].lower(), int(fields[1]), int(fields[2]), int(fields[3]),
        #                                   int(fields[1]), fields[0], fields[5])
        #     # fields[3] represent the last variable which is name, this will be store in self.name
        #     # the rest are similar as above fields[3]
        #     self.items.append(item)
        #     self.items.append(puzzle_item)
        #     # append
        #
        # return self.items

    def get_location(self, x: int, y: int) -> Optional[class_location.Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        if x < 0 or y < 0 or x >= len(self.map) or y >= len(self.map[0]):
            # This is the case where one of them is out of bound
            return None
        elif self.map[x][y] == -1:
            # This is the case where the number is -1 on the map
            return None
        else:
            # # Return the location
            # return class_location.Location(self.map[x][y])
            location_index = self.map[x][y]
            if 0 <= location_index < len(self.locations):
                return self.locations[location_index]
            else:
                return None

    def first_visit_or_not(self, x: int, y: int):
        """
        Determine whether the location is visited or not.
        This is a helper function for "look" action
        """
        location = self.get_location(x, y)
        if location is not None:
            if location.visited:
                return location.get_brief_description()
            else:
                location.visited = True
                return location.get_brief_description()
        else:
            return "Invalid move"

    def available_actions(self, player: class_player.Player, map_data: list[list[int]],
                          locations: class_location.Location):
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """

        # NOTE: This is just a suggested method
        # i.e. You may remove/modify/rename this as you like, and complete the
        # function header (e.g. add in parameters, complete the type contract) as needed

        x, y = player.x, player.y
        actions = []

        # Check if moving North is possible
        if x > 0 and self.map[x - 1][y] != -1:
            actions.append("North")
        # Check if moving South is possible
        if x < len(self.map) - 1 and self.map[x + 1][y] != -1:
            actions.append("South")
        # Check if moving East is possible
        if y < len(self.map[0]) - 1 and self.map[x][y + 1] != -1:
            actions.append("East")
        # Check if moving West is possible
        if y > 0 and self.map[x][y - 1] != -1:
            actions.append("West")
        actions.append("drop item")

        return actions

    def destroy_location(self, location_name: class_location.Location):
        if location_name in self.locations:
            location_name.is_destroyed = True
            location_name.brief_desc = "The location has been destroyed by a missile."
            location_name.long_desc = "This used to be a super castle. The location has been destroyed by a missile."
            print(f"{location_name} has been destroyed.")
