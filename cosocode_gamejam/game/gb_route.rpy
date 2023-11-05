init python:
    import random

label gb_route:
    scene placeholder_bg
    scene bg sept with Dissolve(1.0)
    pause

    scene bg black with Dissolve(1.0)
    #play sound "audio/???"                #(Alarm goes off at 6:00) #(no minigame/pressing it once, bro just wakes up)
    #show bg gb_bed_wakeup with dissolve          #gets up
    gb "{i}Right! First day! Time for me to make a memorable entrance!{/i}"

    play sound "audio/girlbeastcalm.wav"
    show bg gb_bathroom with dissolve                #(goes to bathroom)
    show bg gb_mirror_face with dissolve                #(studies face with stubble)
    #play sound "audio/???"                #(sigh sound effect)
    gb "{i}Oh, of course... this ole thing...{/i}"
    show bg black with dissolve                
    pause 1.0
    #play sound "audio/???"                #(shaving and water sound effects)
    show bg gb_clean_shaven with dissolve                #(clean shaven)
    gb "{i}That's more like it. Now...{/i}"
    show bg gb_doing_makeup with dissolve                #(doing makeup! Maybe show time passing visually, images of actions switching)
    #play sound "audio/??"                 #time ticking sound
                                        #(potential eyeliner/all the makeup as minigame? Eyeliner mouse so straight lines very difficult)
    gb "{i}No one ever told me eyeliner would be this difficult! I definitely should've tried this out before today...{/i}"
                                        #(more minigame)
    gb "{i}Ah damn it, no eye liner!{/i}"
    #play sound "audio/??"                 #(makeup wiping/water soundeffect)

    gb "{i}Eyeshadow and highlighter will have to do{/i}"
    #play sound "audio/??"                 #(some doing stuff sound)
    #show bg gb_makeup_result with dissolve                #(show result. Not perfect, room to improve, but its okay)
    show bg bg_black with dissolve  
    gb "{i}There we go! Now...{/i}"
    window hide
    show bg black with dissolve 
    #play sound "audio/??"                 #picture 
    show gb_selfie with dissolve 
    pause 1.0
    hide gb_selfie with dissolve 
    #show bg gb_clock with dissolve                #(look at time)
    #play sound "audio/??" 
    gb "{i}Oh shoot! Gotta hurry{/i}"
    #play sound "audio/??"                 #(taking bag and running sound effects)

    scene bg black with Dissolve(1.0)
    play sound "audio/girlbeastschool.wav"
    #show bg gb_school with dissolve                #(show school)
    gb "{i}Here we go again{/i}"
    #play sound "audio/??"                 #(walking sound effect)
    #show bg gb_hallway with dissolve                #(hallway)
    #play sound "audio/??"                 #(sound effects of people talking)

    show bg gb_school_happy with dissolve                #(drawing of gb happy)
    gb "Oh this? Yeah, I decided to try some makeup today! Why? Don't know, thought it could be fun! I mean, you girls do this most mornings, no? I wanted to see what the fuss is about!"
    #show ??? with dissolve                #Woman (laugh friendly.)
    #play sound "audio/??"  

    rando "Right, but makeup is for girls, Matteo"
    show bg gb_school_pointing with dissolve 
    gb "Hmm?"
    rando "I know you're gay and all"
    rando "Everyone knows"
    rando "But could you even try to pretend you're normal?"
    gb "No?"
                                        #(insert fake smile minigame)
    image smile animated:
            "happy click"
            pause 0.4
            "neutral click"
            pause 0.4
            "bad click"
            pause 0.4
            "neutral click"
            pause 0.4
            repeat
    show smile animated with dissolve

    menu:
        "{i}I manage to keep up a fake smile{/i}":
            jump gb_succeed

        "{i}I don't manage to keep up a fake smile{/i}":
            jump gb_fail

label gb_succeed:
    scene bg gb_smile_success with Dissolve (0.1)
    #play sound "audio/??"                 #(laughing)
    gb "{i}It's okay, he's just joking around. He thinks its funny, so…I should too! I did choose to do this myself. Anything they say to me is my own fault, not theirs! I won't bring it up.{/i}"
    gb "Yeah yeah. Well, I just thought it could be fun! Wanted to try it out haha. No harm in that!"
    #show ??? with dissolve                #(eyeroll)
    rando "Yeah, well, it looks weird on you anyways" 
    #play sound "audio/??"                 #(leaves, hide sprite?)

    show bg gb_disgruntled_hallway with dissolve 
    #play sound "audio/??"                 #(laughing)
    gb "Haha..yeah…"
    jump gb_continue

label gb_fail:
    scene bg gb_smile_fail with dissolve                #(unbelievable smile/no smile)
    rando "What? You offended? Christ you're sensitive, Matteo. Fucking crybaby."
    gb "I'm-"
    gb "{i}Gosh he's right. I brought this upon myself. I shouldn't feel this upset about it. God damn it.{/i}"
    "{i}I knew people might be assholes about it! Come on, Matteo, man up!{/i}"
    gb "I'm just tired"
    show bg gb_strained_smile with dissolve                #(strained smile)
    rando "Yeah yeah"
    #play sound "audio/??"                 #(bell rings)
    rando "Suppose I'll see ya. Or not."
    #play sound "audio/??"                 #(leaves)
    gb "Yeah…"
    #play sound "audio/??"                 #(people go to class)
    show bg gb_disgruntled_hallway with dissolve 
    jump gb_continue
 
label gb_continue:

    gb "{i}Maybe I shouldn't have done this…People already freaked out last year when I began dressing more…effeminately.{/i}"
    gb "{i}I know they got used to it, but this…{/i}"
    gb "{i}Isn't this a bit much?{/i}"
    gb "{i}Okay okay, don't cry.{/i}"
    gb "{i}I do not need the makeup smudging to be added onto this pile of problems.{/i}"
    #play sound "audio/??"                 #(breath)
    gb "{i}Right. Good…calm. I'm calm. I'll just…go to class and forget about this.{/i}"
    #play sound "audio/??"                 #(walking sound)
    show bg gb_hallway with dissolve                #(goes to class)
    #play sound "audio/??"                 #(quiet chatter)

    scene bg black with Dissolve(1.0)
    show bg gb_class with dissolve                #(kui oleks pilti klassist, gb istumas)
    pause 0.5

    #siit tuleb nvl, muuda ümber
    #kasuta nvl narratorit internal mõtete jaoks??
    #kas neid choice asju saab teha üldse selles telefoni asjas...
    #play sound "audio/??"                 #(phone buzzes in class)
                                        #hea oleks kui siia saaks mingi. phone image ja open animation aga lmao (opens)
    bb_nvl "Hey, you free?"
    nvl_narrator "{i}Oh god, that's never good. Does she need my help right now? I'm still feeling a bit shaken…{/i}"
    nvl_narrator "{i}But…{/i}" #kas need on ka nvl mode või läheb tagasi tavalisse kasti korra, nagu ta tõstaks pead? siis võiks image ka olla
    nvl_narrator "{i}But she's my friend! Come on, I can do this.{/i}"
    gb_nvl "Yep! What's up?" #kas ma saaks need narration sõnumid nagu. ära kaotada kui ta vastab?
                                        #(insert consoling minigame)
                                        #(success bar on the side?)
                                        #(insert consoling minigame)
                                        #(success bar on the side?)

    bb_nvl "I'm sorry to message you like this, I just really needed a distraction"
    pause
    menu:
        "It's alright! Are you okay?":
            pause
            gb_nvl "It's alright! Are you okay?"
            bb_nvl "Not really."
        "Don't worry about it. What happened?":
            pause 0.2
            gb_nvl "Don't worry about it. What happened?"
            bb_nvl "School happened"
        "I was bored in class anyways":
            pause 0.5
            gb_nvl "I was bored in class anyways"
            bb_nvl "Well, hopefully my problems will provide some entertainment"

    bb_nvl "First day of school and I've already managed to lock myself in the bathroom."
    bb_nvl "How pathetic is that?"
    menu:
        "Oh my, are the people there not nice?":
            gb_nvl "Oh my, are the people there not nice?"
            bb_nvl "No, or well, at least the people seem fine."
        "That's not pathetic! It's normal to get overwhelmed by school!":
            gb_nvl "That's not pathetic! It's normal to get overwhelmed by school!"
            bb_nvl "I mean, is it? No one else seems as affected."
        "I'm sorry that happened":
            gb_nvl "I'm sorry that happened"
            bb_nvl "Eh, not much you can do abt it. "

    bb_nvl "I really don't like this new school. I fucking hate it. It's massive! There's so many people and so many classrooms! It's awful."
    bb_nvl "I miss you, Gel."
    menu:
        "I miss you too":
            gb_nvl "I miss you too"
            bb_nvl ":("
        "Hey hey, think about it! You can still come visit! I'm not that far!":
            gb_nvl "Hey hey, think about it! You can still come visit! I'm not that far!"
            bb_nvl "That's true I suppose..."
        "Hey, the people here aren't any kinder. Maybe you'll find some nice people!":
            gb_nvl "Hey, the people here aren't any kinder. Maybe you'll find some nice people!"
            bb_nvl "Maybe..."

    bb_nvl "But hey! Enough about me"
    bb_nvl "How has your first day been?"
    bb_nvl "I saw the photo you sent me earlier. Good job on the makeup! It suits you."
    gb_nvl "Thanks!"

    nvl_narrator "{i}Should I tell her what happened? I know she asked about my day, but...{/i}"
    menu: 
        "It's been good! No issues so far!":
            gb_nvl "It's been good! No issues so far!"
            jump gb_lie 
        "It's been okay, but I did get some annoying comments from a classmate":
            gb_nvl "It's been okay, but I did get some annoying comments from a classmate"
            jump gb_truth

label gb_lie:
    bb_nvl "That's great to hear! Glad to know at least one of us is having a good day :D" 

    #nvl ends here?
    #play sound "audio/??"                    #(phone closing click?)
    show bg gb_class_frown with dissolve                   #gb putting the phone down and frowning?
    gb "{i}Yeah... its better if she thinks everything has gone perfectly{/i}"

    scene bg black with Dissolve(1.0)
    play music "audio/girlbeastcalm.wav"
    show bg gb_removing_makeup with dissolve                   #(look in mirror and take off makeup,look at self)
    gb "{i}God I really am an idiot. What was I thinking! This whole makeup idea was ridiculous!{/i}"
    show bg gb_looking_at_self_frown with dissolve                   #(scrub scrub, frown)
    #play sound "audio/??"                    #(scrub scrub, rustling clothes?)
    gb "{i}I can't let that idiot get to me...even if I know he's right. I just...{/i}" 
    #play sound "audio/??"                    #(takes breath)
    gb "{i}I'm fine. I won't let myself not be fine. I'll just...{/i}"
    gb "{i}Never do that again…{/i}"
    gb "{i}…{/i}"
    gb "{i}Not without a cause{/i}"
    window hide
    show bg gb_mirror_mean with dissolve                   #(insert mirror scene- more mean)
    pause 4.0
    scene bg black with Dissolve(1.0)                  #(sleep time, prob black screen?)

    return

label gb_truth:
    
    bb_nvl "Really?? What assholes! People really need to get out of their own asses about these things. You look nice, that's all that matters!" 

    #nvl ends here?
    #play sound "audio/??"                    #(phone closing click?)
    show bg gb_class_frown with dissolve                   #scene change, of gb putting the phone down and smiling?
    gb "{i}That dork...she always says the dumbest, but nicest things{/i}"
    
    scene bg black with Dissolve(1.0)
    play music "audio/girlbeastcalm.wav"
    show bg gb_removing_makeup with dissolve                     #(look in mirror and take off makeup,look at self)
    gb "{i}Hm. I suppose I really didn't do half bad.{/i}"
    show bg gb_looking_at_self_smile with dissolve                   #(smiled)
    #play sound "audio/??"                    #(scrub scrub, rustling clothes?)
    gb "{i}I should really practice before deciding to wear makeup to school, though...I think I'll stick to being outgoing with clothing for now. Even if I like how makeup looks on me...{/i}"
    window hide
    show bg gb_mirror_okay with dissolve                   #(insert mirror scene-less mean)
    pause 4.0
    scene bg black with Dissolve(1.0)                   #(sleep time, prob black screen?)
    pause 1.0

    return
