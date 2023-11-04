init python:
    import random

$ ynum = renpy.random.randint(427,1030)
$ xnum = renpy.random.randint(260,677)

label bb_route:
    scene placeholder_bg
    show bg sept with Dissolve(1.0)
    pause
    show bg black with Dissolve(1.0)
    #hide bg sept
    
    play sound "audio/alarm.ogg"                         #(Insert very annoying alarm beeping)
    bb "Mnghh....."
    hide bg_black with Dissolve(1.0)
    # seda black->phone alarm transitioni smoothimaks?
    
   
    #--------------------------------------
    
    # minigame here to shut off alarm?
# smth with pulling the thingy to the side?
    show phone animated
    call screen phoneAlarmBlinking
    hide bg black with Dissolve(1.0)
    #seda on vist ainult ühe korra vaja nii et ma teen praegu siin lic?
    #show alarm_background with phone_appear


    #--------------------------------------
    
label bb_next:
    hide phone animated
    stop sound

    show bg black with Dissolve(1.0)
    play sound "audio/bedsheets.wav"  
    bb "I really don't want to go.."
                            #(sheets ruffling sound effect)
    
    show bg room with dissolve                        #(insert room view and bro rubbing his eyes)
    #hide bg black with Dissolve(1.0)
    bb "{i}Right...new school...new...me?{i}" 
    bb "As if."
    
    show cg mirror with dissolve                      #(look in mirror)
    bb "..."
    bb "Let's just get this over with."
                                                    #(insert really dramatic low perspective of a school to make it look intimidating)
    hide cg mirror with dissolve
    show bg stairs with dissolve                        #(insert nervous side view of B)
    bb "{i}Why did I have to be put into such a massive school? {/i}"
    bb "{i}How am I even meant to figure out where all my classes are? I don't know a single person here, so I can't even ask anyone!{/i}"
    
    #---------------------------------
    #(Overlapping text to show distress)
    
    bb "{i}What if I walk into the wrong classroom and don't notice?{/i}"
    bb"{i}They'll all think I'm an idiot.{/i}"
    bb"{i}I'll look ridiculous!{/i}"
    bb"{i}What if they all start hating me?{/i}"
    bb"{i}It's only the first day, I can't make a fool of myself immediately!!{/i}"
    #-----------------------------------

    bb "{i}Come on, Laura, get ahold of yourself!!{/i}"
    show bg hallway with fastdissolve
    play sound "audio/crowd1.ogg"
    #(insert slightly startling transition and scary B colour scheme hallway)
    bb "{i}What was the room I was told to go to?{/i}" 
    bb "{i}100...106? Or was it 108…{/i}"
    bb "{i}How are these classrooms even numbered?{/i}"
    bb "{i}There can't be over a hundred classrooms in this building{/i}"
    bb "{i}...can there?{/i}"
    bb "{i}How many students is that?{/i}"
    $ renpy.music.set_volume(5.00, delay=1.0, channel='sound')
    bb "{i}Hundreds...hundreds and hundreds of students...{/i}"
    
    show bg hallway with dissolve:
        blur 16                                        #(mingi asi, nt blur effect, näitab kuidas ta end tunneb.Visual         
        #show light_animated                            #representation of overwhelming things. lights,              #Loud noises, 
        #show people with (edasi tagasi animatsioon)    #many people, 
        #with zoom=0.33 (äkki?või variation)            #little room, not knowing where to go)

    bb "{i}any one of them could see me, and I wouldn't even know...{/i}"

    #(everything getting a bit louder and uncomfortable to listen to)
    #(insert blurred text of smn tryna speak)

    #hide light_animated
    $ renpy.music.set_volume(0.1, delay=1.0, channel='sound')
    #stop sound fadeout 1.0
    #-------------------------------------

    #(minigame to focus on their words(just quick clicking game with timelimit))

    #-------------------------------------
    show u shadow with fastdissolve
    u "Hello? Are you new here?"
    bb "Eugh...yes, yes I am"
    show u idle with fastdissolve
    u "Oh! So am I! What's your class?"
    bb "10A... or so I've been told, at least"
    u @ smile"Well, thank my lucky stars, same goes for me! "
    u "Do you want to go find the class together perhaps? I can't seem to navigate at all!"
    bb "...sure. Yes, that would be...very nice."
    
    "(unlocked person: friendly classmate from 10A)"
    hide u idle with dissolve
    scene bg class with dissolve #In class: (sits at back)
    $ renpy.music.set_volume(2.0, delay=1.0, channel='sound')
    $renpy.sound.play("audio/tinitus.ogg", loop=True)
    #play sound "audio/tinitus.mp3": on loop #(still overwhelmed buzzing, heart beat sound and yes no focus)
    t "Karl?"
    u "Present"
    t "Hendrik?"
    u "Present"
    t "Maria?"
    u "Present"
    t "Laura?"
    bb "{i}...{/i}"
    $ renpy.music.set_volume(0.00, delay=1.0, channel='sound')
    t "Laura?"
    t "Do we have Laura in here?"
    bb "... here."
    #(raise hand button)
    t "Ah, there you are!"
    $ renpy.music.set_volume(1.00, delay=1.0, channel='sound')
    #play sound "audio/tinitus.mp3" on loop #(back to unfocused buzz)
    bb "{i}God I feel sick. I might actually fall over at this rate.{/i}"
    bb "{i} Why am I so stressed? I found the right class!{/i}"
    bb "{i}I did react a bit slow to her calling my name...but I reacted! {/i}"

    bb "{i}At least...come on, be positive! Mother is always nagging you to be more optimistic!{/i} "
    bb "{i}Come on come on...{/i}"
    bb "{i}I hope no one can hear my breathing.{/i}"
    bb "{i}I'm being loud, aren't I?{/i}"
    bb "{i}Come on, come on...They all probably think I'm disgusting.{/i}"
    bb "{i}I'm sweating, what is wrong with my body!{/i}"
    #play sound "audio/kell.ogg" #(clock ticks 1 minute)

    bb "{i}How long are these classes anyways?{/i}"

    "end for now"


