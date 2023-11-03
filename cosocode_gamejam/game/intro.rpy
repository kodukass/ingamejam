label intro:
    $ quick_menu = False
    #show nighten e1m2_b

    define bb = Character("boneBeast", image="boneBeast")
    define gb = Character("gelatoBeast", image="gelatoBeast")

    # NVL characters are used for the phone texting
    define bb_nvl = Character("boneBeast", kind=nvl, image="phone_bb_icon", callback=Phone_SendSound)
    define gb_nvl = Character("GelatoBeast", kind=nvl, image="phone_bg_icon", callback=Phone_ReceiveSound)

    #nvl_narrator "Nighten added Eileen to the group"
    #n_nvl e2m2_b "Hey! Welcome to the demo Eileen!"
    #e_nvl "who's this?"
    #n_nvl e2m1_b "haha, silly you"
    gb_nvl e2m2_b "Hey Bones. Did ya get there safe?"
    bb_nvl "Yeah I did. God, I HATE long bus rides"
    gb_nvl e2m1_b "3 hours isn`t all that bad"
    #gb_nvl e1m2_b "We talked about showing off the phone the other day, remember?"
    #bb_nvl "it's today? {image=phone_send_icon.png}"
    bb_nvl "It´s still a lot!"# {image=emoji/sweat.png}"
    bb_nvl "The new apartment is nice at least. Got my computer set up and everything"
    gb_nvl e2m2_b "At least there´s that."#" {image=emoji/clap.png}"
    #bb_nvl "Nothing magical, it's just a {a=https://www.renpy.org/doc/html/text.html#text-tag-image}image tag{/a} :)"
    gb_nvl e1m2 "You excited to see what this new school has to offer?"
    bb_nvl "Fuck no. But it´s not like I get a say in it"#{image=emoji/camera.png}"
    #show nighten e1m2_b
    #bb_nvl "{image=EileenSelfieSmall.png}"
    gb_nvl e2m1_b "Can´t be worse than our old school."
    bb_nvl e2m1_b "At least I knew all the people there! And hey, what do you mean ´our´ old school, you stayed! It´s still your school!"
    gb_nvl e2m1_b "I´d gladly take your place if I could, Bones"
    bb_nvl e2m1_b "What, move away from all your friends? Really?"
    gb_nvl e2m1_b "It could be fun! And I´d make new friends!"
    bb_nvl e2m1_b "Sure you would, Gel."
    bb_nvl e2m1_b "But hey, check out this breathtaking view!"
    bb_nvl "{image=EileenSelfieSmall.png}"
    gb_nvl e2m1_b "Woooowwww, love the pavement. You can really see the tax payer money keeping the cement from cracking!"
    bb_nvl e2m1_b "Yeah yeah. Anyways, I gotta go. Talk to ya later!"
    gb_nvl e2m1_b "Bye bye!"

    "Choose your character"
    menu:
        "GB":
            jump gb_route
        "BB":
            jump bb_route