# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    babel = Character("Babel",  what_slow_cps=10) #young ai servant also the MC 
    lucia = Character("Lucia") #rich heiress
    kaine = Character("Kaine") #doctor


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room #this should be the ship bg 

    call lucia_room #start in lucia's room 
    #fade or blink transition to new bg as you look around
    
    jump main_room


    # This ends the game.

    return
