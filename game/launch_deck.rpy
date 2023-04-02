#launch deck

#https://www.reddit.com/r/RenPy/comments/udej2l/how_do_i_make_a_sprite_jump/
transform jumper: #adjust the yoffset as necessary to your preference
    ease .06 yoffset 24 
    ease .06 yoffset -24 
    ease .05 yoffset 20 
    ease .05 yoffset -20 
    ease .04 yoffset 16 
    ease .04 yoffset -16 
    ease .03 yoffset 12 
    ease .03 yoffset -12 
    ease .02 yoffset 8 
    ease .02 yoffset -8 
    ease .01 yoffset 4 
    ease .01 yoffset -4 
    ease .01 yoffset 0


#scene C:
label launch_deck:

    scene launch_deck_goo
    # play sound "muted siren"

    "(Compared to the other rooms, the ship hangar is fairly clean.)"

    "(You walk through and inspect the pods. All the escape pods capable of sustaining life are still parked. No one has escaped.)"

    babel "..."

    "(You find the terminal."

    show terminal

    babel "Retrieving data....."

    scene launch_deck_f with Dissolve(0.7, alpha = True) #clean version

    show noah_swipe with dissolve
    "(A man is crouched in the ship hangar. He’s swiping his keycard at the door lock of his ship.)"

    noah "My key... Why isn’t my key working?!"

    babel "Excuse me-"
    hide noah_swipe
    show noah_look at jumper
    pause
    pause
    return
        # xpos 0.88 ypos 1.28 xanchor 0.5 yanchor 1.0 zoom 0.5

    
    "(The man catches sight of you over his shoulder and begins to scream, throwing himself back.)"

    noah "HOLY SHIT!! GET AWAY FROM ME"

    babel "Sir?"

    show noah_cover zoom .5  
    hide noah_look
    "(He shields his face from you with his arm, backing himself up against the ship.)"

    babel "Is everything all right? How may I be of service?"

    "(Your sensors detect an elevated heartbeat and body temperature. There is a tremor in his hands and his eyes are bloodshot. It’s possible that this user is under the influence of amphetamines.)"

    "(He doesn’t appear to be in enough danger for you to override your customer service protocol.)"

    show noah_groan with fade 
    hide noah_cover
    "(Suddenly, he throws a hand over his forehead and groans in pain.)"

    noah "My head..."

    "(Running a database scan…..User Identity confirmed.)"

    "(Noah Williams. A retired PANDORA executive who resigned a few months ago. He has multiple degrees in astrobiology and plans to teach at a university when we return to Earth.)"

    babel "Can I help you?"

    show noah_disgust with fade
    hide noah_groan
    noah "No." 

    noah "I don’t want to be anywhere near you. You disgust me."

    babel "Thank you for your feedback. I’m sorry to hear your experience on the PANDORA has been less than stellar."

    noah "Jesus." 

    "(The user takes another moment to look you up and down. His gaze is different from the others somehow.)"

    noah "You’re a monument to our depravity."

    "(You cock your head questioningly)"

    noah "Humans. The depravity of humans."

    noah "They find a beautiful thing, and indubitably the first thing they do is enslave it."

    "(Something about him interests you.)"

    babel "Is that why you’re leaving?"

    "(What compelled you to say that? Running diagnostics in 3..2..1….)"
    "(....Diagnostics indicate all functioning is unimpeded…….)"

    babel "........"

    noah "No. I am leaving because PANDORA and I no longer have shared goals."

    noah "Mankind is compelled to project our nature onto the world. We, in our arrogance, think of ourselves as a great work worthy of superimposing a deity."

    noah "The custodian had come to believe it is the creator."

    "(He seems to straighten as he speaks, his hands balling into fists)"

    noah "We forget that we emerged from microbes and muck. We are made of the same substance we seek to control.Kaine has lost sight of that."

    noah "That bastard synonymizes knowledge with moral superiority. He thinks himself merciful for the most basic of decencies."

    "(His face scrunches up in a complex emotion.)"

    noah "Now that you exist, they won’t ever stop."

    "(You consider scanning him for his vital signs but decide against it.)"
    "(You’re not sure what you would do if the customer service algorithm was lifted.)"

    noah "They’ll keep climbing…and climbing…  thinking there is something at the top of this evolutionary mountain."

    "(Even without scans, you can see that he is unwell.)"

    noah "But they are all wrong. The shape of life is not a pyramid."

    show noah swipe:
        ease .5 zoom 1.5 xoffset 100 yoffset 50 #moves right 100px, bottom 50px. set to 0 when you return later.

    show noah_sweat with fade
    hide noah_disgust
    "(He’s gasping for breath, sweat dripping down his chin.)"

    noah "It’s a circle."

    noah "Push too far, and you’ll end right where you started."

    return with fade 
