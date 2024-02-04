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
import class_puzzle

# Note: You may add helper functions, classes, etc. here as needed

# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    win_need_score = 20
    w = class_World.World(open("map.txt"), open("locations.txt"), open("items.txt"))
    p = class_player.Player(0, 0, 30)
    world_map = w.load_map(open("map.txt"))
    adv_location = w.load_location(open("locations.txt"))
    world_items = w.load_items(open("items.txt"))

    menu = ["look", "inventory", "score", "quit", "back"]

    combine_item_puzzle = class_puzzle.CombineItem(hint="What two items can be combined to get what you want?",
                                                   required_material=['Stone', 'Abrasive_tool'],
                                                   combined_item='Stone_Key')
    open_chest_puzzle = class_puzzle.OpenChest(hint="What item can you use to open the chest?",
                                               combined_item="Stone_Key", chest_location=8, final_item="T-card")
    missile_launch_puzzle = class_puzzle.MissileLaunch(hint="Walk around the campus to see if you can find "
                                                            "any hint for the password?", launch_pad="launch_pad",
                                                       password=1890169, sealed_item="Cheat_Sheet",
                                                       target_loc="Super_Castle")
    businessman_trading_puzzle = class_puzzle.BusinessmanTrading(hint="Trade wisely, some items are "
                                                                      "crucial for your success.", business_location=10,
                                                                 crucial_item=["Cheat_Sheet", "T-Card", "Stone",
                                                                               "Abrasive_tool", "Stone_Key",
                                                                               "launch_pad"], exchange_item="Lucky_Pen")

    # location = w.get_location(p.x, p.y)
    # for items in world_items:
    #     if location.loc_number == items.current_position:
    #                 p.pick_up_item(items)
    # lst = p.menu_actions("inventory", w.world_map, w.adv_location)
    # if lst == "Your inventory is empty":
    #     i = 0
    # else:
    #     print("You have the above items")
    #     choice = input("\nDrop Which One?").lower()
    #     i = 0
    #     for items in world_items:
    #         if choice == items.name:
    #             p.drop_item(items, location.loc_number)
    #             if items.target_position == location.loc_number:
    #                 p.score += items.target_points
    #                 print("You successfully drop one item at the correct place \n")
    #                 print("You have received ")
    #                 print(items.target_points)
    #                 print(" points")
    #         else:
    #             i += 1
    #     if i == len(world_items):
    #         print(choice + " is not in your inventory.")

    # ------------------------------------------------------------------------------------------
    # location = w.get_location(p.x, p.y)
    # for items in world_items:
    #     print(items.current_position)
    #     if location.loc_number == items.current_position:
    #         print("found")
    #         p.pick_up_item(items)
    # ------------------------------------------------------------------------------------------

    # a = p.player_look(w.load_map(open("map.txt")), w.load_location(open("locations.txt")))
    # print(a)

    print("Welcome to the Text Adventure Game(UofT version)")
    name = input("Please enter your name to continue: ")
    print("hi, " + name + ". You can now choose to enter the game by entering enter, "
                          "the rules will show up immediately, enter quit to quit the game ")
    print("Your starting location will be  ROBARTS LIBRARY   ")
    choice = input("\nEnter action: ").lower()
    if choice == "enter":
        print("RULES AND PROMT")
        print("Loading...")
        print("You have started the game, Good Luck!")
        while not p.victory:
            location = w.get_location(p.x, p.y)
            # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
            # Depending on whether or not it's been visited before,
            # print either full description (first time visit) or brief description (every subsequent visit)
            actions = []
            location_actions = []
            special_actions = []
            print("Above is what you just done! What to do next? \n")
            print("You can choose to call [menu]")
            print("and these are the list of actions you can perform at this location: ")
            if location is not None:
                for action in w.available_actions(p, w.map, location):
                    actions.append(action)
                print("   Available movements: " + " ,".join(actions))
                for location_action in location.available_actions():
                    location_actions.append(location_action)
                print("   Other actions: " + ", ".join(location_actions))
                special_actions = class_puzzle.available_action(p, w, businessman_trading_puzzle)
                for special_action in special_actions:
                    special_actions.append(special_action)
                print("   Special actions: " + ", ".join(special_actions))
            choice = input("\nEnter action: ").lower()
            if choice in ["north", "south", "west", "east"]:
                p.go_direction(choice, w.map, w.locations)

            elif choice == "pick up":
                i = 0
                for items in world_items:
                    if location.loc_number == items.current_position:
                        p.pick_up_item(items)
                    else:
                        i += 1
                if i == len(world_items):
                    print("You can pick up the air on the floor, will you?")

            elif choice == "drop item":
                lst = p.menu_actions("inventory", w.world_map, w.adv_location)
                if lst == "Your inventory is empty":
                    continue
                else:
                    print("You have the above items")
                    choice = input("\nDrop Which One?").lower()
                    i = 0
                    for items in world_items:
                        if choice == items.name:
                            p.drop_item(items, location.loc_number)
                            if location.loc_number == items.target_position:
                                p.score += items.target_points
                                print("You successfully drop one item at the correct place \n")
                                print("You have received ")
                                print(items.target_points)
                                print("points")
                        else:
                            i += 1
                    if i == len(world_items):
                        print(choice + " is not in your inventory.")

            elif choice == "combine":

                if not p.inventory:
                    print("You have nothing to combine.")
                else:
                    print("You have the following items: ")
                    p.menu_actions("inventory", w.world_map, w.adv_location)
                    item1 = input("Choose the first item to combine: ").lower()
                    item2 = input("Choose the second item to combine: ").lower()
                    if combine_item_puzzle.combine_item(p):
                        print("You have successfully combined to create Stone_Key.")
                    else:
                        print("These items cannot be combined.")

            elif choice == "open_chest":
                if open_chest_puzzle.open_chest(p, w):
                    print("You have successfully opened the chest and found T-card.")
                elif open_chest_puzzle.combined_item not in p.inventory:
                    print("You don't have the required item to open the chest.")

            elif choice == "type_password":
                if "launch_pad" in p.inventory:
                    player_input = int(input("Enter the password: "))
                    if missile_launch_puzzle.use_launch_pad(p, player_input, w):
                        print("Correct password! Super_Castle has been destroyed by the missile you just launched,"
                              " and you suddenly see Cheat_Sheet fly to your hands due to the explosion.")
                    else:
                        print("Incorrect password. Try again.")

            elif choice == "trade":
                curr_location = w.get_location(p.x, p.y).loc_number
                if curr_location == 10 and not businessman_trading_puzzle.traded_or_not:
                    print("Available items to trade: " + ", ".join(p.inventory))
                    item_to_trade = input("Which item would you like to trade? ").lower()
                    businessman_trading_puzzle.trade(p, item_to_trade)

            if choice == "[menu]":
                print("Menu Options: \n")
                for option in menu:
                    print(option)
                choice = input("\nChoose action: ").lower()
                if choice == "quit":
                    print("The world will be unsaved, quiting game now...")
                    print("You can exit whenever you want")
                    break
                else:
                    p.menu_actions(choice, w.world_map, w.adv_location)

            if p.score >= win_need_score:
                print("You have achieve the necessary score to have 100% on the time! Are you continuing?")
                choice = input("\nEnter Yes or No: ").lower()
                if choice == "yes":
                    p.victory = True
                    print("Congratulation on Achieve 100 on the exam!")
                else:
                    continue
    else:
        print("The world will be unsaved, quiting game now...")
        print("You can exit whenever you want")

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
