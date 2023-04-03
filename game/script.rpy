# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:

    babel = Character("BABEL",  what_slow_cps=15, who_bold= True) #young ai servant also the MC 
    lucia = Character("LUCIA", who_bold = True) #rich heiress
    kaine = Character("KAINE", who_bold = True) #doctor
    noah = Character("NOAH", who_bold = True) #teacher
    babelSprite = False
    s = Character("SIREN", color="#c0262b",what_color = "#c0262b", who_bold = True)

    visitAud = False
    visitDin = False
    visitLaunch = False

    credits = ('Prima Sun', 'scenario'), ('Prima Sun', 'writing'),('Tiffany Chen', 'programming'), ('Tiffany Chen', 'sprites'), ('Lesley Chen', 'programming'), ('Lesley Chen', 'sprites'), ('Alex Ouyang', 'programming'), ('Alex Ouyang', 'backgrounds'), ('Eddie Jones', 'music'), ('Eddie Jones', 'sound design')

    credits_s = "{size=60} Credits\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=30}" + c[0] + "\n"
        credits_s += "{size=20}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=20}Backgrounds taken from royalty-free images; some sound effects taken from Apple Loops and freesound.org."

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    call lucia_room from _call_lucia_room #start in lucia's room 
    #fade or blink transition to new bg as you look around
    
    jump main_room


    # This ends the game.

    return
