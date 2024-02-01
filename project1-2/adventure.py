"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
import class_player
import class_World

# Note: You may add helper functions, classes, etc. here as needed

# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":

    w = class_World.World(open("map.txt"), open("locations.txt"), open("items.txt"))
    p = class_player.Player(0, 0, 30)
    world_map = w.load_map(open("map.txt"))
    adv_location = w.load_location(open("locations.txt"))

    menu = ["look", "inventory", "score", "quit", "back"]
    # a = p.player_look(w.load_map(open("map.txt")), w.load_location(open("locations.txt")))
    # print(a)

    while not p.victory:
        location = w.get_location(p.x, p.y)

        # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # Depending on whether or not it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)
        actions = []
        location_actions = []
        print("What to do? \n")
        print("[menu]")
        print("List of actions you can perform at this location: ")
        if location is not None:
            for action in w.available_actions(p, w.map, location):
                actions.append(action)
            for location_action in location.available_actions():
                location_actions.append(location_action)
            print("Available actions: " + ", ".join(actions + location_actions))
        choice = input("\nEnter action: ").lower()
        if choice in ["north", "south", "west", "east"]:
            p.go_direction(choice, w.map, w.locations)

        if choice == "[menu]":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")
            if choice == "quit":
                print("The world will be unsaved, quiting game now...")
                print("You can exit whenever you want")
                break
            else:
                p.menu_actions(choice, w.world_map, w.adv_location)

        # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
        #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
        #  the choice the player made was just a movement, so only updating player's position is enough to change the
        #  location to the next appropriate location
        #  Possibilities:
        #  A helper function such as do_action(w, p, location, choice)
        #  OR A method in World class w.do_action(p, location, choice)
        #  OR Check what type of action it is, then modify only player or location accordingly
        #  OR Method in Player class for move or updating inventory
        #  OR Method in Location class for updating location item info, or other location data etc....
