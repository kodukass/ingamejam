#conf

#gb route stuff

define bb_nvl = Character("BB", kind=nvl, color="#7dcc4b", image="bb", callback=Phone_ReceiveSound)
define gb_nvl = Character("mc", kind=nvl, color="#683e95", image="gb", callback=Phone_SendSound)

#bb route stuff (not important rn)

#define b_bb_nvl = Character("BB", kind=nvl, color="#5f953e", image="bb", callback=Phone_SendSound)
#define b_gb_nvl = Character("GB", kind=nvl, color="#5f953e", image="gb", callback=Phone_ReceiveSound)

#misc

define bb = Character("BB", color="#5f953e", image="bb")
define gb = Character("MC_Name", color="#8e5e9e", image="gb")
define rando = Character("?", color="#d1f024")

define choose_character="choose_character.png"
image bg bg_1sept="bg_1sept.png"
image bg bg_black="bg_black.png"
image bg alarm_background="alarm_background.png"

image bg gb_doing_makeup="gb/applyup.png"
image bg gb_school_pointing="gb/gayshame.png"
image bg gb_school_happy="gb/idle talking gb and friend.png"
image bg gb_smile_fail="gb/losesmile.png"
image bg gb_removing_makeup="gb/makeremove.png"
image bg gb_mirror_mean="gb/mirrorgmeh.png"
image bg gb_mirror_okay="gb/mirrorgsmile.png"
image bg gb_mirror_face="gb/toshave.png"
image bg gb_clean_shaven="gb/shaved.png"
image bg gb_smile_success="gb/winsmile.png"

image gb_happy_click="gb/happy click.png"
image gb_bad_click="gb/bad click.png"
image gb_neutral_click="gb/neutral click.png"
image gb_selfie="gb/selfietosend.png"

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

init -1 python:
    phone_position_x = 0.3
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/SendText.ogg")

init:
    $ mc = 0
    # # Fades to black, then to the new scene.
    $ fade = Fade(0.7, 0, 0.7)
    # # Dissolves between old and new scenes.
    $ dissolve = Dissolve(0.5)
    $ fastdissolve = Dissolve(0.2)

# bb route phone blinking
image phone animated:
            "alarm1"
            pause 0.5
            "alarm2"
            pause 0.8
            repeat

# bb route phone clickable highlight
screen phoneAlarmBlinking:
    imagebutton:
        focus_mask True
        idle "alarm3"
        hover "alarm4"
        action Jump("bb_next")
        #action Jump("phoneAlarmSlider")
        #Show(phoneAlarmSlider)

#screen phoneAlarmSlider:
    #hide phone animated
    #image alarm_background with phone_appear


# bb route phone alarm slider
screen alarmSlider:
    frame:
        has hbox

        vbar value Preference("sound volume")

#sshake
init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,time,child,add_sizes=True,**properties)

        Shake = renpy.curry(_Shake)
init python:
    import random
init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=30)

screen choose_character_buttons():
    imagemap:
        ground choose_character
        hotspot(1122, 307, 566, 545) action Jump ("gb_route") hovered ShowTransient("the_img", img="choose_character_hovergb.png") unhovered Hide("the_img")
        hotspot(246, 295, 552, 544) action Jump ("bb_route") hovered ShowTransient("the_img", img="choose_character_hoverbb.png") unhovered Hide("the_img")

screen the_img(img):
    add img