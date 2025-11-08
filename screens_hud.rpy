# screens_hud.rpy — simple, stable HUD shown when you call:  show screen hud

screen hud():
    zorder 90

    frame:
        xalign 1.0
        yalign 0.0
        background Solid("#000000cc")
        padding (14, 12)

        vbox:
            spacing 6

            text ("Day {d}  •  {seg}  •  {t}").format(
                d=gs.day_number,
                seg=gs.get_time_segment().title(),
                t=gs.time_str()
            )

            text ("Cash: ${c}").format(c=gs.cash)

            hbox:
                spacing 18
                textbutton _("Journal") action ShowMenu("journal_screen")
                textbutton _("Inventory") action ShowMenu("inventory_screen")
