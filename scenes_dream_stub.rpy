# scenes_dream_stub.rpy
# Placeholder Dream night. No combat yet; offers wake or pretend face.

label dream_stub:
    $ gs.time_segment = "dream"
    # If we arrived before midnight boundary, clamp to 00:00-ish.
    if gs.clock_minutes >= 24*60:  # exactly midnight
        pass
    elif gs.clock_minutes >= 22*60:
        $ gs.set_clock(24,0)
    else:
        $ gs.set_clock(0,30)
    scene black
    with fade
    narr "The Dream smells like salt and warm electronics. Something listens. Something taps the glass."
    jump dream_stub_menu

label dream_stub_menu:
    menu:
        "In the Dream…"
        "Face the thing (not implemented)":
            narr "You step forward. The floor dips like a held breath. Systems whir; then nothing. (Combat not implemented yet.)"
            $ journal_note_dream("flooded_heart", "Flooded Heart", "Emotional", "It got louder when I tried to ignore it.", status="seen")
            jump dream_stub_menu
        "Wake up":
            # New day begins; wake at 08:00
            $ gs.advance_day()
            $ gs.set_clock(8,0)
            $ world.new_day_roll()
            jump day_router
