# screens_main_menu_extras.rpy — robust main menu with safe fallback background

screen main_menu():
    tag menu
    add (gui.main_menu_background if hasattr(gui, "main_menu_background") else Solid("#000"))

    frame:
        style "main_menu_frame"
        xalign 0.5
        yalign 0.5
        has vbox
        spacing 10

        text (config.name or "Tsukidere") size 48 xalign 0.5

        textbutton _("Start") action Start()
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Gallery") action ShowMenu("gallery_stub_screen")
        textbutton _("Epilogues") action ShowMenu("epilogues_stub_screen")
        textbutton _("Quit") action Quit(confirm=True)

screen gallery_stub_screen():
    tag menu
    frame:
        align (0.5, 0.5)
        has vbox
        spacing 10
        text "Extras — Stub" size 32
        text "CG Gallery, FEAR/FORM, and other goodies will live here later."
        textbutton "Back" action ShowMenu("main_menu")

screen epilogues_stub_screen():
    tag menu
    frame:
        align (0.5, 0.5)
        has vbox
        spacing 10
        text "Epilogues — Stub" size 32
        text "Post-ending epilogue snippets will be browsable here."
        textbutton "Back" action ShowMenu("main_menu")
