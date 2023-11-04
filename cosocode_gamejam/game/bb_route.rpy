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
    $ renpy.music.set_volume(500.00, delay=1.0, channel='music')
    play music "audio/boyslow_calm_tired.wav"
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
    play music "audio/boybeast.wav"
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
    scene bg black with dissolve #In class: (sits at back)
    $ renpy.music.set_volume(2.0, delay=1.0, channel='sound')
    $renpy.sound.play("audio/tinitus.ogg", loop=True)
    play music "audio/boynervous1.wav"
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
    play sound "audio/clock.wav" #(clock ticks 1 minute)

    bb "{i}How long are these classes anyways?{/i}"
    bb " {i}When do any of my classes end?{/i}"
    bb" {i}I don't want to be here…{/i}"
    bb" {i}I can't handle this right now.{/i}"
    bb" {i}I need to get out.{/i}"
    bb" {i}I need to just…get out and calm myself.{/i}"
    bb"..."
    bb" {i}I don't want to speak up.{/i}"
    bb" {i}I don't want to bring more attention to myself.{/i}"
    bb"{i}...come on, I can do this. I need to… get the courage and just bite the bullet{/i}"
    #(maybe fast click to motivate them to speak up)
    bb "...Miss?"
    t "Yes?"
label toiletpart:
    bb "I'm really sorry, but, may I use the restroom?"
    t "Oh, uh..sure! It's the first day, so you won't fall behind!"
    #(leaves room)
    play sound "audio/door.wav" #door sound effect)
    
    #(insert rapid breathing sound effect)
    show bg toilet with dissolve
    play music "audio/boynervous2.wav"
    #(everything blur except for a bathroom sign)
    play sound "audio/speed_walk.wav"
    play sound "audio/door.wav"
    "..."
    #(fast walking sound effect, door open close)
    #(the entire place is empty. Leaning on sink, looking down)
    #show bg toilet1 with fastdissolve
    #(insert un-winnable calm down minigame with the breathing or clicking or whatever)
    play sound "audio/breathing.wav" loop
    bb "{i}This is not helping, this is not working...{/i}"
    bb"{i}Its not working!!{/i}"
    bb"{i}!!!{/i}"
    bb"{i}I need to think of something else, I'm driving myself mad!{/i}"
    bb"{i}I need a distraction...{/i}"
    show cg phonetoilet with dissolve #(opens phone)
    #(messages GB)
    bb_nvl "Hey, you free?"
    #...
    gb_nvl "Yep! What's up?"
    ""
    #(show visually them calming down while messages scroll by on the phone)
    #(shit unblurs and they feel better)
    #(close phone. School bell rings)
    hide cg phonetoilet with dissolve
    play sound "audio/deep_breath.wav"
    bb"..."
    play sound "audio/door.wav"
    #(Deep breath sound effect)
    #(door open sound effect)
    show bg hallway1 with dissolve
    bb "{i}Let's just go home...{/i}"
    show bg black with dissolve
    #(time skip to home)
    #(sound effect of just laying down on bed. Face planting, if you will)
    play music "audio/boynervous3.wav"
    show bg room1 with dissolve 
    play sound "audio/bedsheets.wav"  
    bb "..."
    #(phone buzz)
    show bg room2
    play sound "audio/RecieveText.ogg"
    #(open chat room)
label q:
    gb_nvl "Hey! You still down to play? I know you got bummed out at school, sooo, it could be fun!"
    bb_nvl "Hmmm..."


    nvl_narrator "{outlinecolor=#386838}I still feel a bit...off from school. What if he can tell through the call? I don't want to bring down the mood...But a game sounds fun...{/outlinecolor}"
    
    menu:
        "Play the game":
            jump gamebb
        "Don't play":
            jump nogame

label gamebb:
    nvl_narrator "A game wont hurt. Besides, Matt always has a way to cheer me up!"
    bb_nvl "You know what, sure! Let me set up rq"
    #(insert sounds of grabbing headphones and whatnot)
    show bg gaming1 with dissolve
    #(BB with headphones)
    #(insert the game/the sounds of the game they play)
    $ renpy.music.set_volume(0.10, delay=1.0, channel='music')
    play music "audio/keyboard.wav" loop

    bb_nvl "Soo, how was your first day?"
    gb_nvl "It was good! I'd ask about yours, but.."
    bb_nvl "Yeah. We already had that conversation. Thanks again by the way, the distraction really helped"
    gb_nvl "Any time!"
    bb_nvl "Mmh… well anyways, care to help me clear out this field?"
    #(game sounds)
    gb_nvl "…You know what's one thing I hate about school?"
    bb_nvl 'What, you? Mr "Straight-A-student"?'
    gb_nvl "Oh shut up! I'm allowed to…take this stuff seriously."
    bb_nvl "I'm just teasing."
    #…
    bb_nvl "Well…? What is it?"
    gb_nvl "Oh, right. It's having to shave each morning. I have a constant razor burn! If my chin were to become sentient, I would probably get strangled in my sleep."
    bb_nvl "That's not the school's fault, though. That's your own choice!"
    bb_nvl "No one is forcing you"
    gb_nvl "Technically, no, but I despise how I look with stubble! At least during summer, people don't see me every day!"
    #…
    gb_nvl "The worst part of growing older was me getting a beard. Curse my father and his immaculate mustache."
    bb_nvl "I thought beards were like…a point of pride for you guys"
    gb_nvl "I mean, guess it can be"
    gb_nvl " They look great on some folks!"

    gb_nvl "I just don't think it fits my face."
    bb_nvl "I suppose. The clean look does suit you quite well."
    gb_nvl "Thanks"
    #…
    bb_nvl "I think having a beard could be cool, though."
    gb_nvl "You're weird, Laura! I can't imagine either of us with a beard!"
    bb_nvl "That sounds like your issue to deal with."
    bb_nvl "Now, you gonna help me or nah?"
    gb_nvl "Im on my way."
    ""
    show bg black
    hide bg gaming1 with dissolve
    #show bg black with dissolve
    "Few hours later..."
    #hide bg black with dissolve
    show bg gaming1 with dissolve
    #(mingisugune visual aid to show time pass, i.e, clock)
    
    nvl_narrator 'You hear your mom say "Laura! You going to sleep?"'
    nvl_narrator '"Yes mom!"'
    bb_nvl "Sorry Matt, I gotta go"
    gb_nvl "Awe man! Sure, talk to you tomorrow, aight?"
    bb_nvl "Yeah yeah"
    ""
    #(call close)
    stop music
    show cg standup with dissolve
    bb"Hmm..."
    #(stand up)
    show cg mirror with dissolve
    bb"..."
    #(go to mirror)
    show cg mirrorbeard with dissolve
    bb"..."
    #(picture's self with beard)
    show cg mirror with dissolve
    bb "Haah..."
    bb "Guess I should go to bed."
    #(Mirror scene with zooming in and comments abt body)
    #(sleep time)
    show bg black with dissolve
    return

label nogame:
     
    bb_nvl "I'm sorry, I'm not really feeling up for it."
    gb_nvl "That's fine! Another time?"
    bb_nvl "Yeah, sure"
    ""
    #(closes phone, stares at ceiling)

    bb "It's better like this. I won't stress him out or cause him any more issues...yeah...Better.."
    #(face go sad)
    show cg sad with dissolve 
    bb "Haah..."
    #(cover face)
    show cg cover_face with dissolve
    bb "God, I'm pathetic..."
    #(grabs phone)
    show cg scrolling with dissolve
    pause
    #(doom scrolling)
    #(start filling up screen slowly yk)
    #(show time flying by)
    show bg black
    hide cg scrolling with dissolve
    #show bg black with dissolve
    "Few hours later..."
    show cg scrolling with dissolve
    #hide bg black with dissolve
    u "Laura! You going to sleep?"
    bb "Yeah, yeah mom!"
    #(sigh)
    #(stands up)
    #(look in mirror)
    #(highlighted insecurities or smth)
    #(can zoom in)
    #(hiirega highlighted??)
    #(end scene with sleep)
    show cg standup with dissolve
    bb"Hmm..."
    #(stand up)
    show cg mirror with dissolve
    #(go to mirror)
    bb "Haah..."
    bb "Guess I should go to bed..."
    show bg black with dissolve
    return

    "end for now"


