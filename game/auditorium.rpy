#auditorium room

define lt = Character("LAB TECH", who_bold = True)
#scene A:
label auditorium:

    scene auditorium_goo
    
    # Sound: no siren.

    "(You can’t hear the siren anymore. This room is soundproof.)"
    "(There’s some mucus on the walls, but it mostly pools underneath the seats.)"

    if babelSprite == True:
        show babel neutral
    babel "....."
    hide babel neutral

    #SHOW TERMINAL HERE

    "(There’s a terminal on your right-hand side. It appears to be functional.)"

    if babelSprite == True:
        show babel neutral
    babel "Retrieving data..."
    hide babel neutral

    scene stagelights with Dissolve(0.7, alpha = True) #clean version
        
    "(The audience applauds uproariously.)"

    "(You’re on the stage, and there’s a man in a suit standing over you. It takes a few seconds for your optometric rods to adjust to the spotlight.
    You are blinded by its beam.)"
    
    show kaine_smile
    kaine "Every once in a while, an invention comes along that revolutionizes everything."

    "(Kaine Edelweiss. My creator.)"

    kaine "The wheel. The steam engine. Nuclear fission. The Theory of Evolution."
    kaine "This is a moment that I have been awaiting for fifteen years, because today….I have been blessed with the honor to present to you such a discovery."
    hide kaine_smile

    "(There’s a screen behind him depicting still images and videos of Kaine and his team.)"

    show kaine_smile
    kaine "Thirty years ago, we discovered the Seed of Life. I was only a deputy then. Never did I imagine that one day, 
    I would be the one leading our team into our civilization’s new panacea."
    hide kaine_smile

    # [Show object asset *Seed of Life*]

    show kaine_smile at right
    kaine "Please allow me to introduce..."

    "(He gestures towards you.)"

    kaine "Babel." 

    "(Kaine leans down and gestures towards you.)"

    kaine "Come here, my boy. Step into the light."

    "(You take his hand and walk forward, downstage.)"

    kaine "I’m sure you must be thinking ‘Yet another AI assistant?’, but I assure you– Babel is much more than that." 

    if babelSprite == True:
        show babel neutral
    babel "Hello, world."
    hide babel neutral

    show kaine_smile
    "(Kaine chuckles at that.)"

    kaine "A private joke between us."
    kaine "Tell us about yourself, Babel."
    hide kaine_smile
    
    "(The audience is enraptured with you.)"

    if babelSprite == True:
        show babel neutral
    babel "My name is Babel. I am a semi-artificial intelligence developed from biohybrid tissue using the Seed of Life." 

    "(The audience explodes into hushed whispers. Could it be? Have humans finally created a being with sentience? Have humans created life?)"

    "(The demonstration continues. Kaine opens the discussion to the audience and you answer questions about all sorts of subjects. Famous artists. History. 
    The Fibonacci sequence.)"

    "(The investors love you. One in particular eyes you from a high VIP seat.)"

    kaine "Modern science has been a journey into the unknown, with a lesson in humility waiting at every stop. But in the face of such cosmic challenges, 
    humanity has endured. Not only have we survived, we have defied all expectations to become a space-faring civilization." 

    kaine "The cosmos will not conquer us. Because we are the cosmos. We are the stuff of stars. This world belongs to us."

    kaine "The future belongs to us!"

    "(The audience explodes into thunderous applause.)"

    # [dev visuals: bg fades to black]

    # [dev visuals: transition to SCENE A1 (bg still black)]

    scene black with Dissolve(0.5, alpha = True)
    jump scene_a1
    
    return 

#scene A1: auditorium backstage/lab
label scene_a1:
    scene research_room_f with Dissolve(0.7, alpha = True)

    lt "(hissing) The tadpoles started uncontrollably growing at the accelerated pace– even ones that weren’t in the room. 
    Hell, some of them weren’t even in the same building!"

    kaine "You’re saying that the Seed was able to affect a wide radius of subjects simultaneously? That’s a miracle. That’s amazing!"

    lt "I’m saying that the tadpoles were connected somehow." 

    lt "That living organisms are connected somehow. And the Seed was able to work through that connection. We couldn't stop it. 
    It could have contaminated the rest of the ecosystem. We had to kill every single one of those tadpoles, Kaine." 

    lt "This technology is too dangerous. We need to push back our timeline."

    kaine "Are you daft? We can’t afford to slow down." 
    kaine "Babel, come here." 

    "(You walk over to Kaine. He grabs you by the shoulders and turns you around to face the tech, whose face has drained of all color.)"

    kaine "Look at this creature. Look at what we were able to create with the Seed."

    kaine "Consciousness. Sentience. True life." 

    kaine "We have evolved from creations into creators. And our world is better for it."

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


    kaine "Look at you… you’re humanity’s greatest triumph."

    kaine "Handing you over to that airhead Lucia Cass felt like giving a microwave to a monkey. 
    She’ll never be able to appreciate you the way I do."

    kaine "There are two kinds of power in our world: money, and knowledge."

    kaine "The PANDORA was built to bring these two together."

    lt "This feels wrong." 

    kaine "Again with the feelings. You know, this is what’s wrong with your kind." 

    lt "I’m sorry?"

    kaine "Incapable of appreciating the beauty of the life around us. Born with your head encased in the dirt, 
    only waiting for the rest of the body to join you. The unlearned. The uneducated." 

    kaine "Do you reckon Curie was scared when she started her work?"

    "(Perhaps she should have been.)"

    kaine "And you will get the fuck back to work." 

    jump main_room
 
