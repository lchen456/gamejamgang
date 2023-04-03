#dining hall

define cw = Character("CAMERAWOMAN", who_bold = True)
#scene B:
label dining_hall:

    scene dining_hall_goo
    
    # bg is dining hall (goo version)
    # Sound: sirens.

    "(You find the terminal immediately.)"
    "(It looks like this room is fairly undamaged, save for some pulsing mucus around the dining table.)"

    show charging_station

    babel "Retrieving data……"

    scene dining_hall_f with Fade(0.7, 2.0, 0.7, alpha=True)

    "(The table is laden with delicacies from every corner of the world.)"
    "(Rows upon rows of delectable dishes– gold-dusted foie gras, fresh truffles, aged caviar and a variety of meats from extinct animals.)"

    cw "Thank you so much for doing this interview, Lucia. "

    show lucia laugh with dissolve

    lucia "I assure you, the pleasure is all mine!"

    hide lucia laugh

    "(Lucia gestures to the lavish hall. You are all sitting at the head of the ornate mahogany table.)"
    "(Everyone has a plate in front of them but no one is eating, too busy with photographs and light rings.)"

    show lucia smirk

    lucia "Welcome to the PANDORA!"
    lucia "And today, I have got–"

    "(Lucia takes your arm and winks at the camera.)"

    if babelSprite:
        show babel neutral at left
        show lucia laugh at right
    else:
        show lucia laugh
    
    lucia "Everyone’s favorite AI companion with me!!"

    "(She pulls you up into her lap and arranges you like a doll.)"

    if babelSprite:
        show babel neutral at left
        show lucia smirk at right
    else:
        show lucia smirk

    "Babel’s a major part of my life here– the best part, if I’m being honest."

    cw "Your companion was gifted to you by PANDORA as a part of your contract, correct?"

    if babelSprite:
        show babel neutral at left
        show lucia laugh at right
    show lucia laugh

    lucia "Yes! We wanted to raise awareness about Babel, and show people what a boon he can be for humanity."

    cw "That sounds magnificent. Could you tell us more about Babel and his story?"

    if babelSprite:
        show babel neutral at left
        show lucia smirk at right
    else:
        show lucia smirk

    lucia "Babel here was developed from a Seed. The Seed of Life, I mean. We haven’t found another one yet, but our hypothesis is that they exist. For decades, we’ve been working hard to figure out how to create one."

    cw "‘We’ as in the researchers who are on PANDORA’s payroll?"

    lucia "Well you know, I’m something of a scientist myself. I’ve spent my whole life investing in tech. Very successfully, I might add."
    lucia "Babel has done miracles for PANDORA. He’s made miracles with my viewership, too."

    hide lucia smirk
    if babelSprite:
        hide babel neutral

    "(There are some chuckles from the sycophants.)"

    cw "Babel, how are you today? Are you having a good time?"

    menu good_time:
        "It’s a wonderful day. I always have a good time with Lucia.":
            pass
        "It’s a wonderful day. I always have a good time with Lucia.":
            pass

    cw "Wow!! How endearing."

    show lucia smirk

    cw "Lucia, you’re very brave to come all the way out here to raise funds for astrobiology. You’re a trailblazer for all of us."

    lucia "Of course. Why sit like a duck on Earth when discoveries are being made in space?"

    "(Lucia starts playing with your hair, twirling it around her fingertips as she talks.)"

    cw "It must be difficult sometimes, being so far away from family."
    cw "They have always been supportive of your cause."

    lucia "I did have some support from my family– small loans, even less than I would have gotten from the banks, to be frank. Being a self-made woman has taught me perseverance and independence."
    lucia "When I’m going through a rough patch and I miss them more than anything, I remind myself that I’m on a mission. I have to make sacrifices for the good of humanity."

    "(Lucia lowers her voice into a secretive whisper.)"

    lucia "Babel isn’t just an AI. He’s an imagining of what we could be. What humans could become."
    lucia "His cognitive ability is unprecedented. He was able to absorb centuries worth of information in only months. His neuromatter is insanely dense. He has quadruple the amount of a regular baby’s neurons, and they all maintain perfect plasticity!"

    cw "Plasticity? Could you explain more on what that is?"

    show lucia angry

    lucia "It’s like uh, um; related to the growth of your brain cells. Anyways, you wouldn’t understand, and it would take me much too long to teach."

    hide lucia angry

    "(Lucia waves her hand vaguely in the air.)"

    show lucia smirk
    
    lucia "We’ve basically figured out that the Seed can accelerate evolution. Fortunately, we were able to plot a projection of the growth, so we pushed it forward, a sort of– forced evolution. Babel is, in a way, a more evolved version of us."

    "(Lucia squishes her cheek to yours. You can feel her oily makeup smear on your face.)"

    lucia "I don’t mean to hurt you, my poor boy. But Babel is not a complete success. He’s a miracle, certainly, but there’s still much he can’t do. Like procreating, for one!"
    lucia "It’s likely because he was made from dead cell matter. We used necrotic tissue as a base for his brain. "
    lucia "Can’t go into details, of course. NDA and all that, but we’re going to try again."
    lucia "This time, with living tissue. We still don’t have a projection for that evolutionary path, but it will change everything. "
    lucia "That’s why I’m still here."
    lucia "The real evolution is yet to come."

    hide lucia smirk

    cw "That sounds amazing. You can give Babel a friend!"

    "(Lucia laughs.)"

    show lucia laugh

    lucia "Hahaha, yes! Next time I’ll ask them to make a girl. We’ll have a complete set!"

    # fade to black
    jump main_room