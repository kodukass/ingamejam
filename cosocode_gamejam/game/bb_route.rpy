label bb_route:
    "bb route"
    $ MC_Name = bb
    $ mc = "BB"
    #"[MC_Name]"
    #"[mc]"

    define bb = Character("boneBeast", image="boneBeast")
    define gb = Character("gelatoBeast", image="gelatoBeast")

    # NVL characters are used for the phone texting
    define bb_nvl = Character("boneBeast", kind=nvl, image="phone_bb_icon", callback=Phone_SendSound)
    define gb_nvl = Character("GelatoBeast", kind=nvl, image="phone_bg_icon", callback=Phone_ReceiveSound)

    define config.adv_nvl_transition = None
    define config.nvl_adv_transition = Dissolve(0.3)

    nvl_narrator "Nighten added Eileen to the group"
    bb_nvl "Hey! Welcome to the demo Eileen!"
    gb_nvl "who's this?"
    bb_nvl "haha, silly you"
    bb_nvl "We talked about showing off the phone the other day, remember?"
    gb_nvl "it's today? {image=emoji/fear.png}"
    gb_nvl "oops sorry night', I forgot {image=emoji/sweat.png}"
    
    ## e_nvl "Nothing magical, it's just a {a=https://www.renpy.org/doc/html/text.html#text-tag-image}image tag{/a} :)"
    # show nighten e1m2_b
