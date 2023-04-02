#auditorium room

define lt = Character("LAB TECH", who_bold = True)
#scene A:
label auditorium:

    scene auditorium_goo #image of auditorium with goo
    
    # bg is auditorium (goo version)
    # Sound: no siren.

    "(You can’t hear the siren anymore. This room is soundproof.)"
    "(There’s some mucus on the walls, but it mostly pools underneath the seats.)"

    babel "....."

    "(There’s a terminal on your right-hand side. It appears to be functional.)"

    babel "Retrieving data..."

    scene auditorium with Dissolve(0.7, alpha = True) #clean version
        
    "(The audience applauds uproariously.)"

    "(You’re on the stage, and there’s a man in a suit standing over you. It takes a few seconds for your optometric rods to adjust to the spotlight.
    You are blinded by its beam.)"

    #KAINE  

    jump scene_a1
    
    "AWOOGA"

    return 

#scene A1: auditorium backstage/lab
label scene_a1:
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

    return
 
