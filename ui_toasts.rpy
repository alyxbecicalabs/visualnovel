# ui_toasts.rpy — generic toast + quick helpers

screen toast(msg):
    zorder 200
    frame:
        at toast_fade
        background Solid("#000000cc")
        padding (12, 8)
        xpos 0.5
        ypos 0.12
        xanchor 0.5
        text msg

transform toast_fade:
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.25 alpha 0.0

init -1 python:
    def fire_toast(msg):
        renpy.show_screen("toast", msg)
        renpy.restart_interaction()

    def arete_toast(domain, h=0, s=0):
        gs.arete.add(domain, harmony=int(h), strife=int(s))
        fire_toast("Arete · {}  +{} / +{}".format(domain, int(h), int(s)))

    def cash_toast(delta):
        d = int(delta)
        if d >= 0:
            gs.earn(d)
            fire_toast("+${}".format(d))
        else:
            if gs.spend(-d):
                fire_toast("-${}".format(-d))
            else:
                fire_toast("Not enough cash.")
