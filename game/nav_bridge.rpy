
define main = "main song.mp3"
#SCENE 3
label nav_bridge:
     show navigation_bridge_goo

     #[dev notes: stop siren sound, lower volume of general space track]
     play music main volume 0.4

     "(The ship bridge is remarkably quiet.)"

     "(It feels nice.) "

     "(There’s more of the strange, sticky black liquid all over the crew’s seats and control interface, 
     but it’s part of the scenery at this point.)"

     if babelSprite==True:
          show babel neutral
     babel "I wonder..."
     hide babel neutral

     "(You hover over the comms-link array. The lights indicate that the call is still connected.)"

     if babelSprite==True:
          show babel neutral
     babel "Mayday, Mayday. This is AI unit 6626068 reporting from the PANDORA. I require immediate assistance. 
     Please help."
     hide babel neutral

     "(...No response)"

     "(You switch to another channel.)"

     if babelSprite==True:
          show babel neutral
     babel "SOS. SOS. SOS. Accident in PANDORA. In need of rescue. SOS!"
     hide babel neutral

     "(There is no response here either…you check the comm logs for information.)"

     "(You find a strong signal from a few days ago. One that is only sent when a ship goes down– the dead man’s switch. 
     Your neighbor has gone dark. There is no one on the other side.)"

     "(You pull out the control panel. You have to increase the radius of the scope.)"

     if babelSprite==True:
          show babel neutral
     babel "There has to be ships nearby. We can’t have gone that far off course."
     hide babel neutral

     "(The geo-locator isn’t working and you don’t recognize any of the stars through the windows.)"
     "(There is a bot charging terminal on the control panel, but most bots aren’t allowed in the bridge.)"

     # [Dev Notes: show terminal]

     "(It probably doesn’t have any data in it.)"

     if babelSprite==True:
          show babel neutral
     babel "... Might as well." 
     hide babel neutral

     "(You plug yourself in)"

     if babelSprite==True:
          show babel neutral
     babel "Retrieving data....."
     hide babel neutral
