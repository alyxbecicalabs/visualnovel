# screens.rpy — base screens restored (game_menu + notify)

init offset = -1

# A compact, dependency-free game menu container.
screen game_menu(title, scroll=None):
    tag menu
    modal True

    # dim background
    add Solid("#00000088")

    # center frame
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 650
        padding (24, 24)

        vbox:
            spacing 16

            # Title
            text title size 36 xalign 0.5

            # Content area. If caller asks for a scroll viewport, provide it.
            if scroll == "viewport":
                frame:
                    xfill True
                    yfill True
                    padding (0, 0)
                    viewport:
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        ymaximum 520
                        # Insert caller's content inside the viewport.
                        vbox:
                            spacing 10
                            transclude
            else:
                # Non-scrolling content inserted here.
                vbox:
                    spacing 10
                    transclude

            # Footer controls
            hbox:
                spacing 12
                xalign 1.0
                textbutton _("Return") action Return()

# Simple notify used by renpy.notify(...)
screen notify(message):
    zorder 200
    frame:
        background Solid("#000000cc")
        padding (10, 6)
        xpos 0.5
        ypos 0.12
        xanchor 0.5
        text message
    timer 1.8 action Hide('notify')
