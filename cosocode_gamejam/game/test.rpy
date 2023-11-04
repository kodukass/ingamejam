label test:

    "bb route"
    # Main script for the demo!

    define n = Character("mc", image="nighten")

    # NVL characters are used for the phone texting
    define n_nvl = Character("mc", kind=nvl, image="nighten", callback=Phone_SendSound)
    define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

    define config.adv_nvl_transition = None
    define config.nvl_adv_transition = Dissolve(0.3)

    transform transparent:
        alpha 0.0

# ma ei saa aru kuidas seda tööle saada korralikult rn :(
    image phone animated:
            "alarm1"
            pause 0.5
            "alarm2"
            pause 0.8
            repeat

    screen phoneAlarm:

        imagebutton:
            focus_mask True
            idle "alarm3"
            hover "alarm4"
            action Jump("one") 

    screen alarmSlider:
        frame:
            has hbox

            vbar value Preference("sound volume")

    show phone animated
    call screen phoneAlarm