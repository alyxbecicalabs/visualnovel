# scenes_day5.rpy

label day5_entry:
    $ gs.set_time(5, "morning")
    $ world.new_day_roll()
    scene black
    with fade
    narr "Day 5. Your heartbeat finally agrees to use indoor voice."
    $ journal_add_today_event("Day 5 start. Weather: %s; Moon: %s." % (world.current_weather, world.moon_phase))

    menu:
        "Where first?"
        "Library Archives (Theo)":
            jump day5_theo_archives
        "Arcade (Cas) — Ghost Cab recon":
            jump day5_cas_debug
        "Explore Town (free roam)":
            jump town_map

label day5_theo_archives:
    $ gs.adjust_bond("theo", +1)
    scene black
    with dissolve
    th "We can sit on the floor. Archivists do it constantly; it’s praxis."
    menu:
        "Ask what’s missing from the record.":
            $ gs.arete.adjust("Psychological", harmony_delta=1)
            $ arete_toast("Psychological", h=1)
            $ set_flag("THEO_SECRET_STACKS", True)
            $ journal_add_memory("theo", "He keeps a private list of lost names he’s still hunting.")
            $ journal_add_today_event("We talked about what falls out of the record.", "Psych +")
            th "People erased by accident or convenience. We can do better."
        "Ask him to pick a book for you.":
            $ gs.arete.adjust("Spiritual", harmony_delta=1)
            $ arete_toast("Spiritual", h=1)
            $ journal_add_today_event("Accepted a book picked by Theo’s intuition.", "Spiritual +")
            th "This one smells like cedar and rainy bus rides."

    th "Take this—bookmark. It’s spare. Probably haunted by kind intentions."
    $ gs.add_item("archivist_bookmark")
    $ journal_add_today_event("Theo gave me an Archivist’s Bookmark.")
    $ bedtime = time_advance_and_check(55)
    if bedtime:
        jump go_to_bed
    jump day5_post_first

label day5_cas_debug:
    $ gs.adjust_bond("cas", +1)
    scene black
    with dissolve
    cs "Okay. If we find the ghost cab and it boots a menu—don’t touch ‘Wipe’."
    menu:
        "Use the Debug Token.":
            if gs.has_item("debug_token"):
                $ gs.arete.adjust("Psychological", harmony_delta=1)
                $ arete_toast("Psychological", h=1)
                $ journal_add_today_event("We tested the Ghost Cabinet. It… hummed back.", "Psych +")
                cs "It did the thing! I wasn’t hallucinating."
            else:
                cs "We’ll come back when you have the token. …That wasn’t a bit."
        "Play air hockey to stall.":
            $ gs.arete.adjust("Social", harmony_delta=1)
            $ arete_toast("Social", h=1)
            $ journal_add_today_event("Stalled with air hockey and laughter.", "Social +")
            cs "Competitive stalling accepted."

    $ journal_add_memory("cas", "Their bravado hides careful notes. They’re documenting anomalies like a scientist.")
    $ bedtime = time_advance_and_check(45)
    if bedtime:
        jump go_to_bed
    jump day5_post_first

label day5_post_first:
    menu:
        "Do something else before night?"
        "Visit the other friend":
            menu:
                "Choose:"
                "Library Archives (Theo)":
                    jump day5_theo_archives
                "Arcade (Cas)":
                    jump day5_cas_debug
        "Explore Town (free roam)":
            jump town_map
        "Call it a day (sleep)":
            jump go_to_bed

label day5_end:
    jump go_to_bed
