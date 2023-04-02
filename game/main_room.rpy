﻿# main hub that the character returns to after every memory

define here_before = False
define visited = []


label main_room:

    scene bg lobby 

    #SCENE 2
    # knee deep in goo
    show goo 
    "(The moment you step inside, you’re knee deep in goo.)"
    "(It’s everywhere, dripping down the grand staircase and even stuck on the ceiling.)"

    babel "There are no users here."
    babel "Reboot complete."

    "(You spot a charging terminal on the far side of the room, but it appears to have been smashed.)"

    show charging_station
    "Recharge Terminal: A charging station for all bots in service. Contains fuel, software and memory drive backups. 
    There is one in every room on this vessel."

    "(There may be data inside the terminals that can help you to contact HQ for a rescue operation.)"
    hide charging_station 

    babel "Retainer 6626068 reporting in new Priority." 
    babel "Priority #3: Retrieve data from all functional charging terminals. "

    "(You approach an information desk with a map of the vessel.)"
    babel "Scanning PANDORA diagram…" 

    "Most areas of the ship are too damaged to enter safely. You’ve compiled a list of rooms with terminals to search through."
    $ here_before = True
    #SCENE 2 END

    jump lobby_map

    # These display lines of dialogue.
    if here_before:
        babel "Back here again..."
        jump lobby_map

    label lobby_map: 
        show map
        menu:
            set visited
            "Which door should I enter?"

            "Auditorium":
                jump auditorium

            "Dining Hall":
                jump dining_hall

            "Launch Deck":
                jump launch_deck

            "Navigation Bridge":
                jump nav_bridge


            # "Door 3" if "Door 1" in visited and "Door 2" in visited and "Door3" not in visited:
            #     jump door_3

    # if all doors visited, do something here