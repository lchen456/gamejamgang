#auditorium room

define applause = "audio/sfx_applause.mp3"
define murmuring = "audio/sfx_murmuring.mp3"

define lt = Character("LAB TECH", who_bold = True)
#scene A:
label auditorium:

    scene auditorium_goo
    
    stop sound
    # Sound: no siren.

    "(You can’t hear the siren anymore. This room is soundproof.)"
    "(There’s some mucus on the walls, but it mostly pools underneath the seats.)"

    if babelSprite:
        show babel neutral with dissolve
    babel "....."
    hide babel neutral

    #SHOW TERMINAL HERE

    show charging_station at right:
        zoom 0.8
    "(There’s a terminal on your right-hand side. It appears to be functional.)"

    if babelSprite:
        show babel neutral with dissolve
    babel "Retrieving data..."
    hide babel neutral
    hide charging_station

    scene stagelights with Fade(0.5, 0.5, 0.5) 

    play sound sfx_applause volume 0.5  
    "(The audience applauds uproariously.)"

    "(You’re on the stage, and there’s a man in a suit standing over you. It takes a few seconds for your optometric rods to adjust to the spotlight.
    You are blinded by its beam.)"
    
    show kaine_smile with dissolve
    kaine "Every once in a while, an invention comes along that revolutionizes everything."

    "(Kaine Edelweiss. Your creator.)"
    stop sound

    kaine "The wheel. The steam engine. Nuclear fission. The Theory of Evolution."
    kaine "This is a moment that I have been awaiting for fifteen years, because today...I have been blessed with the honor to present to you such a discovery."
    hide kaine_smile

    "(There’s a screen behind him depicting still images and videos of Kaine and his team.)"

    show kaine_smile 
    kaine "Thirty years ago, we discovered the Seed of Life. I was only a deputy then. Never did I imagine that one day, 
    I would be the one leading our team into our civilization’s new panacea."
    hide kaine_smile

    # [Show object asset *Seed of Life*]
    show seed at top
    pause 2
    hide seed
    
    show kaine_smile at right with dissolve
    kaine "Please allow me to introduce..."

    "(He gestures towards you.)"

    kaine "Babel." 

    "(Kaine leans down and gestures towards you.)"

    kaine "Come here, my boy. Step into the light."

    "(You take his hand and walk forward, downstage.)"
    if babelSprite:
        show babel neutral at left
    kaine "I’m sure you must be thinking ‘Yet another AI assistant?’, but I assure you– Babel is much more than that." 
    hide kaine_smile
    hide babel neutral
    
    if babelSprite:
        show babel neutral with dissolve
    babel "Hello, world."
    hide babel neutral

    show kaine_smile
    "(Kaine chuckles at that.)"

    kaine "A private joke between us."
    kaine "Tell us about yourself, Babel."
    hide kaine_smile
    
    "(The audience is enraptured with you.)"

    if babelSprite:
        show babel neutral
    babel "My name is Babel. I am a semi-artificial intelligence developed from biohybrid tissue using the Seed of Life." 

    play sound murmuring volume 0.5 
    "(The audience explodes into hushed whispers. Could it be? Have humans finally created a being with sentience? Have humans created life?)"

    "(The demonstration continues. Kaine opens the discussion to the audience and you answer questions about all sorts of subjects. Famous artists. History. 
    The Fibonacci sequence.)"
    stop sound fadeout 1.0

    "(The investors love you. One in particular eyes you from a high VIP seat.)"
    hide babel neutral

    show kaine_smile with dissolve
    kaine "Modern science has been a journey into the unknown, with a lesson in humility waiting at every stop. But in the face of such cosmic challenges, 
    humanity has endured. Not only have we survived, we have defied all expectations to become a space-faring civilization." 

    kaine "The cosmos will not conquer us. Because we are the cosmos. We are the stuff of stars. This world belongs to us."

    kaine "The future belongs to us!"

    play sound sfx_applause
    "(The audience explodes into thunderous applause.)"

    # [dev visuals: bg fades to black]
    # [dev visuals: transition to SCENE A1 (bg still black)]

    scene black with Fade(0.7, 2.0, 0.5)
    stop sound fadeout 1
    jump scene_a1
    
    return 

#scene A1: auditorium backstage/lab
label scene_a1:

    scene black 

    show kaine_smile 
    kaine "Unless the Seed is on fire, I'm going to be very upset that you've pulled me out of my evening session with Babel"
    hide kaine_smile

    scene research_room_f
    play sound sfx_machinery 

    "(A lab technician stands alone. In his hands is a holo-tablet that displays a live feed of tadpoles.)"

    lt "It’s about the latest investigation. Project CAS324."

    show kaine_smile 
    kaine "That’s the growth acceleration attempt. Did the tadpoles die?"
    hide kaine_smile

    lt "The new findings just don’t corroborate with our previous journals. We can’t publish this until we’re sure of what it is."
    
    lt "The tadpoles started growing uncontrollably at the accelerated pace– even the control group in a separate container. 
    Some of the affected frogs weren’t even in the same room!"
    
    show kaine_smile 
    kaine "You’re saying that the Seed was able to affect a wide radius of subjects simultaneously? That’s a miracle. That’s amazing!"
    hide kaine_smile

    lt "I’m saying that the tadpoles were connected somehow." 

    lt "This experiment proves that living organisms are connected in a way we can’t explain. 
    And the Seed was able to work through that connection. We couldn't stop it. It could have contaminated the rest of the ecosystem. 
    We had to kill every single one of those tadpoles!" 

    lt "This technology is too dangerous. 
    Until we’re sure of how it works, we need to push back our timeline."

    show kaine_smile
    kaine "Are you daft? We can’t afford to slow down." 
    kaine "Babel, come here." 
    hide kaine_smile

    "(You walk over to Kaine. He grabs you by the shoulders and turns you around to face the tech, whose face has drained of all color.)"

    show kaine_smile at right
    if babelSprite:
        show babel neutral at left
    kaine "Look at this creature. Look at what we were able to create with the Seed."

    kaine "Consciousness. Sentience. True life." 

    kaine "We have evolved from creations into creators. And our world is better for it."

    "(Your pain sensor spikes. He’s gripping your shoulders like they were handles.)"

    kaine "Babel. How do you feel about your life?"

    #SHOW “CHOICE”
    menu choice:
        "I am grateful to be alive. It is my joy and pleasure to live and to serve.":
            pass
        "I am grateful to be alive. It is my joy and pleasure to live and to serve.":
            pass
    #END “CHOICE”
    
    kaine "See?"

    "(Kaine cups your cheeks in his hands and looks at you with a pained expression.)" 

    kaine "Look at you...you are humanity’s greatest triumph."
    hide kaine_smile
    hide babel neutral

    pause 0.1
    show kaine_smile
    kaine "Handing you over to that airhead Lucia Cass felt like giving a microwave to a monkey. 
    She’ll never be able to appreciate you the way I do."

    kaine "But I’m prepared to do what’s necessary. To consolidate our research funds."
    hide kaine_smile

    lt "So we sold him for money, is what you mean."

    show kaine_smile
    kaine "There are two kinds of power in our world: money, and knowledge."
    kaine "The PANDORA was built to bring these two together."
    hide kaine_smile

    lt "This feels wrong." 

    show kaine_smile
    kaine "Again with the {i}feelings{/i}. You know, this is what’s wrong with your kind." 
    hide kaine_smile

    lt "I’m sorry?"

    "(You can see his badge. He's a Class-C personnel. He must be new. You consider scanning him in the database, but Kaine probably wouldn’t like that.)"
    
    show kaine_smile
    kaine "You are incapable of appreciating Babel’s beauty. 
    You close your eyes to the truth of creation that we seek– no. You’re blind; you never had eyes at all. 
    I suppose not everyone can understand a {i}visionary{/i} like me." 

    "(Kaine throws an arm around you and leads you away.)"

    kaine "You all were born with your heads encased in the dirt, waiting for the rest of the body to join you. The uneducated. The unlearned."
    kaine "I hired you to clean beakers and monitor cameras. Stay in your lane" 
    
    "(He slams the door shut on the young man and the last thing you see was his face, staring at you with something akin to pity.)"
    hide kaine_smile

    jump main_room
 
