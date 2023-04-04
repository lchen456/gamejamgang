
define main = "audio/mus_main.mp3"
define freewill = False
define fyourself = 0
define cap = Character("CAPTAIN", who_bold = True) 
define c = Character("cREW", who_bold = True)

#SCENE 3
label nav_bridge:
     show navigation_bridge_goo

     #dev notes: stop siren sound, lower volume of general space track
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

     "(There is no response here either… you check the comm logs for information.)"

     "(You find a spike in the signals from weeks ago. One that is only sent when a ship goes down– the dead man’s switch. 
     It’s a recording.)"

     c "This is the SERAPHIM. We are reporting an ongoing incident on board." 

     "(Her voice is shaky. There are strange howling noises in the background. Dogs?)"

     c "We are enroute to Asteroid #KL97 on a sample retrieval mission. "

     c "We have live cargo with us. And also personal animals. In seemingly random order, 
     they’ve undergone an almost instantaneous metamorpho-"

     "(There’s a sound of something like a wet explosion.)"

     c "OH MY GOD, WHAT THE FUCK?!"

     "(She’s screaming. You can almost hear her voice start to shred with distress.)"

     c "CAPTAIN?! CAPTAIN!"

     c "CA-"

     "(The recording ends. She must have stopped pressing the dead man’s switch.)"

     "(Your neighbor has gone dark. There is no one on the other side.)"

     "(You pull out the control panel. You have to increase the radius of the scope.)"

     if babelSprite:
          show babel neutral with dissolve
     babel "There has to be ships nearby. We can’t have gone that far off course."
     hide babel neutral

     "(The geo-locator isn’t working and you don’t recognize any of the stars through the windows.)"

     show charging_station at right with dissolve
     "(There is a bot charging terminal on the control panel, but it’s almost never used.  AI aren’t allowed inside executive rooms.)"

     "(It probably doesn’t have any data in it.)"

     if babelSprite:
          show babel neutral
     babel "... Might as well."  
     "(You plug yourself in)"
     babel "Retrieving data..."
     hide babel neutral
     hide charging_station

label finale:
     # [Dev Notes: show navigation bridge bg clean]
     scene navigation_bridge_f with Fade(0.7, 1.0, 0.7, alpha = True)
     
     "(Lucia is holding your hand and pulling you forward.)"

     "(You’re on the navigational bridge. You’re not supposed to be on the navigational bridge. This is against the rules.)"

     show lucia smirk
     lucia "Come here, dear."
     hide lucia smirk

     "(Kaine is on the bridge, too. What’s going on?)"

     show kaine_smile
     kaine "You’ve been so good for us, Babel." 

     kaine "We’ve been pursuing this line of research for a while now, and we think we’ve made a breakthrough." 

     "(He’s standing next to a table. It’s covered with a green antimicrobial cloth, and on it lay scalpels and forceps. Surgical instruments.)"
     hide kaine_smile

     show lucia smirk
     lucia "Our most important goal right now is to understand the Seed." 
     hide lucia smirk

     show kaine_smile at right
     kaine "But having just one is not enough." 

     show lucia smirk at left
     lucia "We need {i}ore{/i}."

     hide lucia smirk 
     hide kaine_smile
     "(This feels uncomfortably like a conversation between parents and a child they’re leaving at an orphanage.)"

     show kaine_smile
     kaine "My team has calculated a way for us to detect Seeds, but they’re almost impossibly far away, and 
     much too difficult to find precisely without your help." 

     kaine "You were created from the Seed. You have an affinity for it that nothing else in our world does." 

     "(He gestures to a clear, cylinder storage unit sitting on the table. Inside is a fleshy, ribbed object. A brain?)"

     kaine "We have options, of course. This is bio-matter we’ve extracted from a human cerebrum that might work in a pinch. 
     But there’s too much we don’t know about the Seed and how it relates to living beings. We could cause unintended consequences."
     hide kaine_smile

     "(The control panel is open. Its chrome plate cover has been removed and inside is a mess of wires and buttons. 
     The Seed of Life has been set inside.)"

     show seed at top with dissolve
     "(Connected to it is a cylinder vial, large enough to place a brain into.)"
     hide seed

     show kaine_smile with dissolve
     kaine "You are our first choice. You’re our highest chance of success."
     hide kaine_smile

     show lucia smirk with dissolve
     lucia "We need to integrate your central processing unit with the control panel’s framework."
     hide lucia smirk

     "(Lucia comes to stand behind you, brushing your hair to the side as she eyes your nape, where your lock mechanisms are located.)"

     show kaine_smile with dissolve
     kaine "Babel. Will you do us one last favor?"
     hide kaine_smile

     menu eff:
          "Yes. I am happy to be of service.":
               jump noahsark
          "Go fuck yourself.":
               # [dev notes: must click 3 times to choose option]
               if fyourself == 2:
                    $ freewill = True
                    if babelSprite:
                         show babel neutral
                    babel "Go fuck yourself."
                    hide babel neutral
                    show lucia angry at left
                    lucia "Excuse me?"
                    show kaine_smile at right
                    "(Lucia gapes at you. Kaine just stares.)"

               else: #fyourself < 2
                    if fyourself == 1:
                         "I shouldn't say this?"
                    else:
                         "(I shouldn't say this.)"
                    $ fyourself +=1
                    jump eff


label noahsark:
     hide kaine_smile
     hide lucia angry

     stop audio
     "(Suddenly, there’s a loud commotion at the door. A man’s voice begins shouting.)"

     show kaine_smile
     kaine "What the hell, I said we were not to be disturbed!"
     hide kaine_smile

     "(Someone bursts into the room. You can see the security guards knocked out on the floor behind him.)"
     
     show kaine_smile
     kaine "Noah?"
     hide kaine_smile

     show noah_disgust with dissolve
     "(Indeed. It’s Noah Williams. He must have used his high clearance to bypass the alarms. 
     You think his file mentioned some history with Kaine. Former research partners?)"

     noah "{b}You.{/b}"
     hide noah_disgust

     "(He has a gun in hand, pointing at Kaine.)"
     "(He doesn’t look too good, but his eyes are perfectly lucid and razor focused.)"
     
     show kaine_smile with dissolve
     kaine "Don’t shoot!"

     "(Kaine raises both his hands up.)"

     kaine "I know what you want. I’ll delete it. 
     I’ll erase everything. We can take it all down from the web. We’ll make it look like we never found anything at all."
     hide kaine_smile

     "(So much for humanity’s ambassador into the new age.) "

     show noah_disgust
     noah "You’re a bad liar. But even if it’s the truth.."

     noah "Knowledge cannot be unlearned. How will we ever be satisfied with not-doing, when now we know it can be done?"
     hide noah_disgust

     show lucia angry
     lucia "We’ll pay you. How much? "
     hide lucia angry

     "(Noah laughs.)"

     "(While he’s distracted, another guard tackles him from behind.)"

     show noah_groan
     noah "Ooof-"
     hide noah_groan

     "(He drops the gun. Kaine and Lucia pounce on the human brain.)"

     show lucia angry at left
     lucia "We need to install it now. We need to find more Seeds."
     
     show kaine_smile at right
     kaine "But Babel-"

     lucia "There’s a maniac with a gun trying to kill us!! It’s now or never!!!"
     hide lucia angry
     hide kaine_smile

     "(You put yourself between the two of them and the writhing men on the ground. You’re not sure what’s going on, 
     but you’re not supposed to let anyone kill Lucia and Kaine.)"
     
     show lucia angry at left
     show kaine_smile at right
     lucia "How the fuck did he get in?!"
     kaine "He built half this damn ship, that’s how. "
     hide lucia angry
     hide kaine_smile

     "(There’s more shouting from outside. The crew and captain must have gotten wind of what’s happening.)"
     
     show lucia angry at left
     lucia "I’m going to call for more help. I’m not dying here. The world needs me."
     lucia "You finish that damn thing!"
     
     show kaine_smile at right
     kaine "I’M GOING AS FAST AS I CAN."

     hide lucia angry 
     hide kaine_smile

     "(Lucia dodges Noah and the guard and rushes to the door.)"

     show noah_disgust
     "(There’s a sickening crack of bone and flesh. Noah won the fight.)"

     "(He breaks out of the security guard’s hold and lunges at you.)"
     hide noah_disgust

     "(Lucia screams.)"

     show lucia angry
     lucia "BABEL!!"

     lucia "Babel, come with me NOW."

     "(You look at her, coiffed hair ruined and makeup smeared all over her clothes. You don’t really feel like going anywhere.)"
     hide lucia angry

     "(Before you could do anything, a hand encircles your throat and you are bodily launched onto the chromeplate floor.)"

     "(You try to pry his hands off you but he’s too strong… You are pinned under his mass. 
     You have a lot of advantages over humans, but super strength isn’t one of them.)"

     "(Asphyxiating you doesn’t do anything, though. You don’t breathe air.)"

     "(Being an ex-PANDORA executive, he should have been aware of that. Unless he wasn’t in his right mind.)"

     if babelSprite:
          show babel neutral at left
     babel "Am…pheta…mines... for sure…"
     hide babel neutral

     if babelSprite:
          show noah_sweat at right
     else:
          show noah_sweat
     noah "You’ve doomed us with your existence. "

     "(You scan him calmly, ignoring the vice around your throat. His heartrate is 225BPM. 
     His irises are extremely dilated. You can think you can see wet eyelashes and the glittering of tears.)"

     noah "It won’t erase my sin, but the least I can do is destroy you before I die."

     "(He’s at risk of cardiac arrest. You need to call for a medic.)"

     babel "You…need…h-elp.."

     "(Your vocal cords are reinforced with carbon. They are not easily damaged, but it still hurts.)"

     noah "Jesus Christ, I hate that customer service algorithm."

     hide babel neutral
     hide noah_sweat

     "(He lifts your head up by the neck and slams it down. You feel something being dislodged in the hind section of your brain.)"

     #[dev notes: add audio file thunking]

     if babelSprite:
          show babel neutral
     play sound sfx_thud
     babel "Not….customer… ser-"
     stop sound
     hide babel neutral

     "(He does it again)"

     if babelSprite:
          show babel neutral
     #dev notes: add audio file thunking
     play sound sfx_thud
     babel "........"

     hide babel neutral

     show kaine_smile
     "(In the distance, you see Kaine still integrating the brain and the Seed onto the control panel.)"

     "(He’s almost done.)"     
     hide kaine_smile

     if babelSprite:
          show babel neutral
     babel "I am sorry...."
     hide babel neutral

     "(You squeeze your eyes shut. You don’t want to see things you can’t do anything about.)"
     "(Noah has stopped.)"

     if babelSprite:
          show babel neutral
     babel "..that I exist."
     hide babel neutral

     "(You keep trying to push him off. Some things in your skull are loose. He’s doing actual damage now. You could die.)"

     show noah_look
     noah "....."
     hide noah_look

     "(You feel tight, like you cannot breath despite not needing air. 
     You want to run another diagnostic but you suspect it would find nothing, again. 
     You brace your hand on his shoulders, trying to remove him but he doesn’t budge an inch. He’s incredibly solid.)"

     show noah_look
     noah "You.. you’re-"
     stop sound
     
     hide noah_look with dissolve

     #[dev notes: all audio stops except for heartbeat track]
     play sound sfx_heartbeat

     "(Suddenly, your fingers go through him.)"
     "(Something heavy collapses on top of you. A liquid. It splatters all over your face, your hair.)"
     "(Some of it gets into your open mouth.)"

     #[dev notes: heartbeat track still going, add coughing] 
     play sound sfx_cough
     if babelSprite:
          show babel neutral
     babel "COUGH COUGH COUGH COUGH"

     "(It’s cloying and thick. It reeks of blood.)"

     "(You get up, something clattering in your skull. Damage to long term memory storage.)"

     "(Your working memory is only around two hours long. You are no longer capable of retaining memories beyond this time frame.)"

     babel "What’s happening..."
     hide babel neutral

     "(You look for Kaine but he’s gone, too. The control panel is closed. He must have finished his work. 
     There’s more of the dark liquid on the floor where he stood.)"

     "(You make eye contact with the captain and crew, standing on the other side of the bridge.)"

     cap "Ba-"

     "(Soundlessly, they explode. But instead of blood and guts, only a viscous, scarlet black liquid projects into the air, 
     cascading on every surface.)"
     if babelSprite:
          show babel fear
     babel "Somebody.....help..."

     jump nav_scene3b


label nav_scene3b:
     # [Dev Notes: show navigation bridge bg dirty]
     show navigation_bridge_goo

     "(You’re collapsed on the floor, disconnected from the terminal.)"

     "(Now that you know what the goo is, the stickiness of your hair and skin is unbearable.)"

     "(You cannot fix yourself. Only an engineer can repair the damage that Noah did to your cranial processors. 
     You thought you’d find one, but evidently you haven’t, and you probably never will.)"

     "(You check your internal clock. You have around ten minutes before your two hour time limit is up.)"

     "(There are large cracks all over the windows and walls. Small asteroid impacts, with no captain or 
     crew to dodge them. One of them is large enough to leave a hole in the hull.)"

     "(You sit up, strings of the viscous mucus sliding down you and onto the floor.)"

     if babelSprite:
          show babel fear
     babel "Ha….haha…"

     "(Primordial soup. The precursor of life.)"

     "(Noah was right. They pushed it too far, and now all life has reverted to its basest form. A rebirth borne of hubris.)"

     "(You cannot help but feel like everything is a sick joke.)"

     "(You’re tired.)"

     "(You were built to run on fusion energy, but you’ve been on battery reserves. "
     "You could recharge, but the charging station is in Lucia’s room, where you first woke up.)"

     menu:
          "Go outside." if freewill:
               jump outside 
               
          "Go back to charge in Lucia’s room.":
               scene black with Dissolve(1, alpha = False)
               jump credits
     return

label outside:
     scene black
     # [Black screen]
     # [Sound: breathing]
     # [Sound: heartbeat]
     play audio sfx_breathing
     play audio sfx_heartbeat
     play audio sfx_footsteps
     # [footsteps]
     # [Music stops]
     stop audio 
     # [dev note: GOD ENDING Animation]

     show hand_1
     pause 0.5
     hide hand_1
     show black 
     pause 0.5

     show hand_2
     pause 0.5
     hide hand_2
     show black 
     pause 0.5

     show hand_3
     pause 0.5
     hide hand_2
     show black 
     pause 0.5

     # [roll credits]
     jump credits

label credits:
     #CREDITS GO HERE
     #scrolling credits effect credit DaFool, leon, modified by rabcor, with some edits
     play music main 
     scene black

     image logo = "logo.png"
     image splash = "mirror babel_goo.png" 
     image cred = Text(credits_s, text_align=0.5)

     $ credits_speed = 25 #scrolling speed in seconds

     show logo with Fade(0.5, 0.7, 0.5) 
     pause 5.0
     hide logo with dissolve
     show cred at Move((0.5, 2.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
     with Pause(credits_speed - 5)
     show splash behind cred with dissolve 
     with Pause(5)

     stop music fadeout 1

     show text "Thank you"
     return