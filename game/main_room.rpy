# main hub that the character returns to after every memory

label main_room:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show babel neutral

    # These display lines of dialogue.
    if here_before:
        b "Back here again..."

    $ visited = []
    menu:
        set visited
        "Which door should I enter?"

        "Door 1" if "Door 1" not in visited:
            jump door_1

        "Door 2" if "Door 2" not in visited:
            jump door_2

        "Door 3" if "Door 1" in visited and "Door 2" in visited and "Door3" not in visited:
            jump door_3

    # if all doors visited, do something here