#conf

#gb route stuff

define bb_nvl = Character("BB", kind=nvl, color="#7dcc4b", image="bb", callback=Phone_ReceiveSound)
define gb_nvl = Character("GB", kind=nvl, color="#683e95", image="gb", callback=Phone_SendSound)

#bb route stuff (not important rn)

#define b_bb_nvl = Character("BB", kind=nvl, color="#5f953e", image="bb", callback=Phone_SendSound)
#define b_gb_nvl = Character("GB", kind=nvl, color="#5f953e", image="gb", callback=Phone_ReceiveSound)

#misc

define bb = Character("BB", color="#5f953e", image="bb")
define gb = Character("GB", color="#8e5e9e", image="gb")

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