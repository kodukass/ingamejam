init python:
    import random

$ ynum = renpy.random.randint(427,1030)
$ xnum = renpy.random.randint(260,677)

label bb_route:
    scene placeholder_bg
    show bg_1sept with Dissolve(1.0)
    pause
    show bg_black with Dissolve(1.0)
    hide bg_1sept
    #(Insert very annoying alarm beeping)
    bb "Mnghh....."
    
    hide bg_black with Dissolve(1.0)
    #(turning off alarm minigame?)
    show bg_black with Dissolve(1.0)
    hide bg_black with Dissolve(1.0)
    bb "I really don't want to go.."
    #(sheets ruffling sound effect)
    #(insert room view and bro rubbing his eyes)
    #show ??? with dissolve
    bb "Right...new school...new...me?" 
    bb "As if."
    #(look in mirror)
    #show ??? with dissolve
    bb "Let's just get this over with."

    #(insert really dramatic low perspective of a school to make it look intimidating)
    #(insert nervous side view of B)
    bb "Why did I have to be put into such a massive school? "
    bb "How am I even meant to figure out where all my classes are? I don't know a single person here, so I can't even ask anyone!"
    #(Overlapping text to show distress)
    
    #text ("What if I walk into the wrong classroom and don't notice?")
    #“ They'll all think I'm an idiot.”
    #“ I'll look ridiculous!”
    #“ What if they all start hating me?”
    #“ It's only the first day, I can't make a fool of myself immediately!! “
    #“Come on, Laura, get ahold of yourself!!“
    #(insert slightly startling transition and scary B colour scheme hallway)
    #„What was the room I was told to go to? 100...106? Or was it 108…”
    #“ How are these classrooms even numbered?”
    #“ There can't be over a hundred classrooms in this building...can there?”
    #“ How many students is that? “
    #“Hundreds...hundreds and hundreds of students...any one of them could see me, and I wouldn't even know...“
    #(mingi asi, nt blur effect, näitab kuidas ta end tunneb.Visual representation of overwhelming things. Loud noises, lights, many people, little room, not knowing where to go)
    #(everything getting a bit louder and uncomfortable to listen to)
    #(insert blurred text of smn tryna speak)
    #(minigame to focus on their words(just quick clicking game with timelimit))


    #------------------------------------------------------
    "bb route"
    # Main script for the demo!

    define n = Character("mc", image="nighten")

    # NVL characters are used for the phone texting
    define n_nvl = Character("mc", kind=nvl, image="nighten", callback=Phone_SendSound)
    define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

    define config.adv_nvl_transition = None
    define config.nvl_adv_transition = Dissolve(0.3)

    nvl_narrator "Nighten added Eileen to the group"
    n_nvl e2m2_b "Hey! Welcome to the demo Eileen!"
    e_nvl "who's this?"
    n_nvl e2m1_b "haha, silly you"
    n_nvl e1m2_b "We talked about showing off the phone the other day, remember?"
    e_nvl "it's today? {image=emoji/fear.png}"
    e_nvl "oops sorry night', I forgot {image=emoji/sweat.png}"
    n_nvl "No problem, you must be quite busy!"
    n_nvl e2m2_b "congrat on showing the emoji tho {image=emoji/clap.png}"
    e_nvl "Nothing magical, it's just a {a=https://www.renpy.org/doc/html/text.html#text-tag-image}image tag{/a} :)"
    n_nvl e1m2 "But since we use regular renpy, we can use the same principle to send pictures!"
    e_nvl "Right! Let me take a selfie {image=emoji/camera.png}"
    show nighten e1m2_b
    e_nvl "{image=EileenSelfieSmall.png}"
    n_nvl e2m1_b "awww, you look fantastic!"
    show nighten e2m2_b
    e_nvl "A bit low res but hey, the pic has to fit the screen somehow"
    
    n_nvl "Thank you Eileen for doing this demo with me!"
    e_nvl "no problem, I hope people will make good use of it!"
    e_nvl "byyee {image=emoji/wave.png}"


    show nighten:
        ease 0.5 xalign 0.5 

    n e1m2 "That's it for the demo!"
    n normal e1m2 "Do you have any question?"

    jump question

label question:
    menu:
        "What do you want to know?"
        "How is this phone working?":
            n e2m2 "To put it simply, it's just another style for the NVL mode."
            n e2m1 "Yep, it's not much more complicated than that!"
            n e1m1 "The main thing was to make it look like a phone, with a scrollable feed and the correct placement for the text."
            n e1m2 "Knowing that, you can probably build your own phone screen; but mine can still be used as a base if needed!"
            jump question


        "How to add it to my {i}*awesome*{/i} project?":
            n e1m2 "First, add PhoneTexting.rpy to your project directory. Don't forget to edit MC_Name to your main character name!"
            n e2m2 "Then you'll have to edit the nvl screen in screen.rpy, or else it's not gonna work!"
            n e1m2 "In gui.rpy, change gui.nvl_list_length to None, so that messages don't disapear."
            n e1m1 "And you now just have to create nvl characters and made them speak!"
            n e1m2 "If you want to use the regular NVL screen, change the nvl_mode variable to \"classic\", and back to \"phone\" if you want to use it again!"
            n e2m2 "Of course check the more detailed instruction on the project page, but that's all there is to it! You should have something somewhat functionnal at this point."
            jump question


        "Who made this?":
            n e1m1 "The code is created by me, Nighten!"
            n e1m2 "I also drew my sprite and the phone UI, using Krita, Rebelle 3 and Inkscape."
            n "All the source are available in the folder and on {a=https://github.com/NightenDushi}github{/a}, feel free to use it in your project."
            n e2m2 "Credits would be appreciated, but not mandatory!"
            n e1m2 "The background is created by our dear Uncle Mugen! You can find more of his work on {a=https://lemmasoft.renai.us/forums/viewtopic.php?t=17302}LemmaSoft{/a}!"
            jump question
        
        "Why {i}another{/i} phone/messaging system?":
            n e2m2 "Well, mostly because I found the other one available way too complicated, and not really friendly to use."
            n e1m1 "I wanted a system that feels like renpy, so that you can understand it and build on it."
            n e1m2 "And I think more option is great for the community in general!"
            n e2m1 "But I don't think this system is perfect, far from it!"
            jump question
            
        "Nothing, have a good day!":
            jump end

label end:
    n e2m2 "Aww, thank you! Most people just close the game without saying goodbye, so I appreciate it a lot!"
    n e1m2 "If you still have some questions, don't hesitate to message me on Discord {i}(Nighten#3081){/i}!"
    n e1m1 "And if you want further help, you can also hire me as a programmer! {a=https://lemmasoft.renai.us/forums/viewtopic.php?f=66&t=61647}All the details are here{/a}."
    n e2m1 "Take care! I wish you good things in life!"
    $ renpy.quit()