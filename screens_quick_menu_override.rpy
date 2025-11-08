# screens_quick_menu_override.rpy — cleaned & complete

default quick_menu = True

screen quick_menu():
    zorder 90
    if quick_menu and not _in_replay:
        frame:
            background None
            xalign 1.0
            yalign 1.0
            has hbox
            spacing 18

            textbutton _("Back") action Rollback() style "quick_button"
            textbutton _("History") action ShowMenu("history") style "quick_button"
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) style "quick_button"
            textbutton _("Auto") action Preference("auto-forward", "toggle") style "quick_button"
            textbutton _("Save") action ShowMenu("save") style "quick_button"
            textbutton _("Q.Save") action QuickSave() style "quick_button"
            textbutton _("Q.Load") action QuickLoad() style "quick_button"
            textbutton _("Prefs") action ShowMenu("preferences") style "quick_button"

style quick_button is default
style quick_button:
    size 18
    color "#FFFFFF"
    hover_color "#FFFFFF"
    outlines [(1, "#00000099", 0, 0)]
