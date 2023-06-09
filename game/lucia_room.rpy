# The script of the game goes in this file.

# The game starts here.
define audio.siren = "audio/sfx_siren.mp3"

label lucia_room:
    #SCENE 1
    scene black 
    scene lucias_bedroom with Dissolve(5.0, alpha=True) # bg of lucia's room
    
    play sound sfx_siren volume 0.25
    pause 2 #pause 3 seconds for sound?
    s "May I have your attention please...
    May I have your attention please. 
    There is an emergency reported in the building. 
    Please proceed through the nearest exit to the launch pad for evacuation. 
    May I have your attention please…."

    #babel waking up
    babel "97\% . . . 98\% . . . 99\% . . ."
    babel "Reboot complete."
    
    "(Directive 1 . . . ERROR . . . Directive 2 . . . ERROR . . .)"
    stop sound

    "(Neurolink Status: Disconnected. Fusion status...ERROR. Powersource linking to battery...)"

    babel "Welcome aboard the PANDORA! Thank you for choosing us to fulfill all your luxury vacation needs. 
    We invite you to sail with us into the future as together we explore the furthest frontiers of space and human possibility. "  

    play sound sfx_jingle
    pause 2 

    "(Directive 3 . . . ERROR . . . Directive 4 . . . CONNECTED)"
    "(No lifesign visuals detected. Switching to thermo-sensors.)"
    "(No biosignals detected...)"
  
    babel "Directive 4 ARMED. Entering emergency protocol."

    "(New Directive: Locate all remaining users and await instructions. Customer service algorithm terminated.)"
    play sound siren volume 0.25

    s "...there is an emergency reported in the building. Please proceed through the nearest exit to the launch for evacuation. 
    May I have your attention please..."
   
    babel "?"

    "(Running memory scan...No data files in memory drive detected.)"
    "(Default Emergency Protocol voice recording activated.)"

    babel "Retainer 6626068 reporting in. There appears to have been an emergency evacuation of vessel 16180, also known as the PANDORA. Current location coordinates unknown. 
    Pilot and crew status unknown. Visual scans indicate no signs of life."

    "(Your feet are stuck to the chromeplate floor by what appears to be dried, black mucus.)"
    "(The joints in your body are also covered in the same viscous substance. Your movements are slightly impaired.)"
    "(Thermal scans indicate the substance has a temperature of 323.15 Kelvins. The air temperature is 174 Kelvins. 
    Life support systems must be inoperational.)"

    "(Centrifugal acceleration is at 334 Gal – one-third of Earth’s gravity. The centrifugal drive system is operating below capacity.)"

    babel "Priority #1: Rescue. Locate and save possible survivors."

    "(The dark, pulsing liquid substance is splattered all over the ceilings and walls, but appears concentrated on where you were leaning on the wall.)"
    "(An arc of the liquid surrounds your prone form like a halo.)"

    babel "Priority #2: Document and investigate the incident for later analysis."

    "(Apart from the siren, audio sensors pick up nothing.)"
    "(Movement scans detect subtle pulsing from particularly large globs of the goo. 
    This may be a noteworthy point for research after fulfilling Priority #1.)"
    "(There is no sign of violence or damage to the master chamber aside from the contaminant.)"

    #SOUND HERE
    stop sound fadeout 1.0
    pause 2

    menu scene_1_end:
        "Exit Room.":
            #babel's sprite does not show up
            return

        "Stay and Look Around":
            #if babel sees himself in mirror, sprite appears for rest of game, else not
            jump .lucia_room_stay

    label .lucia_room_stay:
        #SCENE 1.5
        
        $ babelSprite = True
        #port window image here?
        "(You look out the port window. Pinpoints of light twinkle in the vast, dark void. They do not match any constellations in your database.)"

        babel "There are multiple pieces of furniture inside this chamber. Cataloging now... Bed, Sofa, Sofa #2, Dresser, Dresser #2, Dresser #3, Vanity, Holoscreen, Mirror."
        scene black with dissolve
        show mirror base with Fade(0.5,0.5,0.5)
        pause 1
        show mirror

        "(The mirror is a vintage artifact from the pre-lightspeed era. It does not require fusion energy to function. You can see your reflection in it.)"
        #show mirror
        image mirror:
            "mirror base.png"
            "mirror babel_goo.png" with Dissolve(3.0, alpha=True)
        
        show mirror babel_goo
        "(There’s nothing left to see here. You leave the room)"

        scene black with Dissolve(0.5, alpha =True)
        return

label lucia_room_end:
    #SCENE END2
    scene lucias_bedroom_goo with Fade(0.5,0.5,0.5) # bg of lucia's room
    
    play sound sfx_siren volume 0.25
    pause 2 

    s "May I have your attention please...
    May I have your attention please. 
    There is an emergency reported in the building. 
    Please proceed through the nearest exit to the launch pad for evacuation. 
    May I have your attention please..."
    stop sound

    if babelSprite:
        show babel neutral
    babel "97\%...98\%...99\%..."
    babel "Reboot complete."
    play sound sfx_jingle

    jump credits