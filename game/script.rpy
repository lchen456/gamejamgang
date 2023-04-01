﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define babel = Character("Babel") #young ai servant also the MC 
define lucia = Character("Lucia") #rich heiress
define kaine = Character("Kaine") #doctor


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room #this should be the ship bg 

    jump lucia_room #start in lucia's room 
    #fade or blink transition to new bg as you look around
    
    jump main_room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"


    # This ends the game.

    return