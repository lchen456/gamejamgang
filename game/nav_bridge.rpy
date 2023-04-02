
define main = "main song.mp3"
define freewill = False
#SCENE 3
label nav_bridge:
     show navigation_bridge_goo

     #[dev notes: stop siren sound, lower volume of general space track]
     play music main volume 0.4

     "(The ship bridge is remarkably quiet.)"

     "(It feels nice.) "

     "(There’s more of the strange, sticky black liquid all over the crew’s seats and control interface, 
     but it’s part of the scenery at this point.)"

     if babelSprite:
          show babel neutral
     babel "I wonder..."
     hide babel neutral

     "(You hover over the comms-link array. The lights indicate that the call is still connected.)"

     if babelSprite:
          show babel neutral
     babel "Mayday, Mayday. This is AI unit 6626068 reporting from the PANDORA. I require immediate assistance. 
     Please help."
     hide babel neutral

     "(...No response)"

     "(You switch to another channel.)"

     if babelSprite:
          show babel neutral
     babel "SOS. SOS. SOS. Accident in PANDORA. In need of rescue. SOS!"
     hide babel neutral

     "(There is no response here either…you check the comm logs for information.)"

     "(You find a strong signal from a few days ago. One that is only sent when a ship goes down– the dead man’s switch. 
     Your neighbor has gone dark. There is no one on the other side.)"

     "(You pull out the control panel. You have to increase the radius of the scope.)"

     if babelSprite:
          show babel neutral
     babel "There has to be ships nearby. We can’t have gone that far off course."
     hide babel neutral

     "(The geo-locator isn’t working and you don’t recognize any of the stars through the windows.)"


     show charger
     "(There is a bot charging terminal on the control panel, but most bots aren’t allowed in the bridge.)"
     # [Dev Notes: show terminal]
     "(It probably doesn’t have any data in it.)"
     hide charger
     if babelSprite:
          show babel neutral
     babel "... Might as well." 
     hide babel neutral

     "(You plug yourself in)"

     if babelSprite:
          show babel neutral
     babel "Retrieving data....."
     hide babel neutral

label nav_scene3b:
     # [Dev Notes: show navigation bridge bg dirty]
     show navigation_bridge_goo

     "(You peel yourself off the control panel that you have collapsed on.)"

     "(Now that you know what the goo is, the stickiness of your hair and skin is unbearable.)"

     "(You feel strange inside, too.)"

     "(You peel away the silicone layer of your skin to peer into your chest cavity.)"

     "(Under the light, the viscous mucus held a red sheen as it dripped out of you.)"

     "(Noah was right. They pushed it too far, and now all life has reverted to its basest form.)"

     "(You cannot help but feel like everything is a sick joke.)"

     "(Primordial soup. The precursor of life.)"

     "(So the humans were successful after all. You were alive.)"

     "(There are large cracks all over the windows and walls. Small asteroid impacts, with no captain or crew to dodge them.)"

     menu:
          "Go outside." if freewill:
               jump outside
          "Go to sleep.":
               scene black with Dissolve(1, alpha = False)
               jump credits

label outside:
     scene black
     # [Black screen]
     # [Sound: breathing]
     # [Sound: heartbeat]
     # [sound: Keypad beeping (opening the door)]
     # [footsteps]
     # [Music stops]
     # [Sound: all audio is silent]
     # [GOD ENDING Animation]
     # [roll credits]
     jump credits

label credits:
     #CREDITS GO HERE

