#launch deck

#scene C:
label launch_deck:

    scene launch_deck_goo

    play sound sfx_siren_muffled fadeout 1.0

    "(Compared to the other rooms, the ship hangar is fairly clean.)"

    "(You walk through and inspect the pods. All the escape pods capable of sustaining life are still parked. No one has escaped.)"

    babel "..."

    "(You find the terminal."

    show charging_station
    babel "Retrieving data....."

    scene launch_deck_f with Fade(0.7, 2.0, 0.7, alpha=True) #clean version
    stop sound

    show noah_swipe with dissolve
    "(A man is crouched in the ship hangar. He’s swiping his keycard at the door lock of his ship.)"

    noah "My key... Why isn’t my key working?!"

    babel "Excuse me-"
    hide noah_swipe

    #jump: https://lemmasoft.renai.us/forums/viewtopic.php?t=26172
    show noah_look:
        xpos 0.35  ypos 0
        yoffset 0
        easein 0.05 yoffset -60
        easeout 0.05 yoffset 0
        easein 0.05 yoffset -30
        easeout 0.05 yoffset 0
        easein 0.05 yoffset -4
        easeout 0.05 yoffset 0
    pause 
    "(The man catches sight of you over his shoulder and begins to scream, throwing himself back.)"

    show noah_look at right 
    noah "HOLY SHIT!! GET AWAY FROM ME"

    babel "Sir?"

    show noah_cover at right 
    hide noah_look 
    "(He shields his face from you with his arm, backing himself up against the ship.)"

    babel "Is everything all right? How may I be of service?"

    "(Your sensors detect an elevated heartbeat and body temperature. There is a tremor in his hands and his eyes are bloodshot. It’s possible that this user is under the influence of amphetamines.)"

    "(He doesn’t appear to be in enough danger for you to override your customer service protocol.)"

    show noah_groan at right
    hide noah_cover
    "(Suddenly, he throws a hand over his forehead and groans in pain.)"

    noah "My head..."

    "(Running a database scan...User Identity confirmed.)"
    play sound sfx_jingle

    "(Noah Williams. A retired PANDORA executive who resigned a few months ago. He has multiple degrees in astrobiology and plans to teach at a university when we return to Earth.)"

    babel "Can I help you?"

    show noah_disgust at right
    hide noah_groan
    noah "No." 
    noah "I don’t want to be anywhere near you. You disgust me."

    babel "Thank you for your feedback. I’m sorry to hear your experience on the PANDORA has been less than stellar."

    noah "Jesus." 
    "(The user takes another moment to look you up and down. His gaze is different from the others somehow.)"

    noah "I feel sorry for you."
    noah "You’re a monument to our depravity." 
    if babelSprite:
        show babel neutral at left with fade    
    "(You cock your head questioningly)"
    hide babel neutral 
    
    noah "Humans. The depravity of humans."

    noah "They find a beautiful thing, and indubitably the first thing they do is enslave it."

    "(Something about him interests you.)"

    babel "Is that why you’re leaving?"

    hide noah_disgust
    if babelSprite:
        show babel neutral
    "(What compelled you to say that? Running diagnostics in 3..2..1...)"
    "(...Diagnostics indicate all functioning is unimpeded...)"
    
    babel "........"
    hide babel neutral

    show noah_look at right
    noah "No. I am leaving because PANDORA and I no longer have shared goals."

    noah "Mankind is compelled to project our nature onto the world. We, in our arrogance, think of ourselves as a great work worthy of superimposing a deity."

    noah "The custodian had come to believe it is the creator."

    "(He seems to straighten as he speaks, his hands balling into fists)"

    noah "Kaine forgets that we emerged from microbes and muck. We are made of the same substance we seek to control."

    show noah_disgust
    hide noah_look
    noah "That bastard synonymizes knowledge with moral superiority. He thinks himself merciful for the most basic of decencies."

    "(His face scrunches up in a complex emotion.)"

    noah "Now that you're a 'success', they won’t ever stop."

    "(You consider scanning him for his vital signs but decide against it.)"
    "(You’re not sure what you would do if the customer service algorithm was lifted.)"

    noah "They’ll keep climbing...and climbing...thinking there is something at the top of this evolutionary mountain."

    "(Even without scans, you can see that he is unwell.)"

    noah "But they are all wrong. The shape of life is not a pyramid."
    hide noah_disgust
    show noah_sweat at center:
        yalign 0.2
        ease 2 zoom 2
    
    "(He’s gasping for breath, sweat dripping down his chin.)"

    noah "{b}It’s a circle.{/b}"

    noah "{b}Push too far, and you’ll end right where you started.{/b}"

    jump main_room
