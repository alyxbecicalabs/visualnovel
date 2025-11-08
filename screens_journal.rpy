# screens_journal.rpy — minimal, uses state_journal.rpy data

screen journal_screen():
    tag menu
    use game_menu(_("Journal"), scroll="viewport"):
        vbox:
            spacing 12
            $ today = journal.day_log.get(gs.day_number, {"summary":"", "events":[]})
            text ("Day [gs.day_number] — [today['summary']]")

            if today["events"]:
                frame:
                    style "menu_frame"
                    viewport:
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        ymaximum 520
                        vbox:
                            spacing 6
                            for e in today["events"]:
                                text "• " + e
            else:
                text "No events logged today."
