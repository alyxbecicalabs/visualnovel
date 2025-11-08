# scenes_day2.rpy

label day2_entry:
    $ gs.set_time(2, "morning")
    $ world.new_day_roll()
    scene black
    with fade
    narr "Day 2. The world feels slightly less heavy if you don’t look directly at it."
    $ journal_add_today_event("Morning walk: air tasted like chalk dust. Weather: %s; Moon: %s." % (world.current_weather, world.moon_phase))

    menu:
        "Where first?"
        "Library (Theo)":
            jump day2_theo_library
        "Arcade (Cas)":
            jump day2_cas_arcade
        "Explore Town (free roam)":
            jump town_map

label day2_theo_library:
    $ set_flag("theo_met", True)
    $ gs.adjust_bond("theo", +1)
    scene black
    with dissolve
    th "You came. Good. I saved a study table—the one that doesn’t wobble."
    menu:
        "Ask what he’s working on.":
            $ gs.arete.adjust("Psychological", harmony_delta=1)
            $ arete_toast("Psychological", h=1)
            $ gs.adjust_trust("theo", +1)
            th "Cataloging oral histories that were never recorded. Which sounds like a contradiction, but… it isn’t."
            $ journal_add_today_event("Theo showed oral history notes—stories that almost didn’t survive.", "Psych +")
        "Make a pun about overdue emotions.":
            $ gs.arete.adjust("Social", harmony_delta=1)
            $ arete_toast("Social", h=1)
            $ gs.adjust_bond("theo", +1)
            $ journal_add_today_event("Made Theo groan-laugh with a bad pun.", "Social +")
            th "…Okay that’s terrible. And I’ll allow it."
        "Ask for a quiet lap of the stacks.":
            $ gs.arete.adjust("Spiritual", harmony_delta=1)
            $ arete_toast("Spiritual", h=1)
            $ journal_add_today_event("Walked the stacks in shared quiet.", "Spiritual +")
            th "Bring your hands to your sides when you breathe. It helps the sound travel less."

    th "Here—temporary pass. If anyone glares, tell them ‘Theo okayed it’."
    $ gs.add_item("library_guest_pass")
    $ journal_add_today_event("Got a Library Guest Pass from Theo.")
    $ journal_add_memory("theo", "He cares about stories that almost didn’t make it.")
    menu:
        "Share something you almost didn’t say.":
            $ gs.arete.adjust("Emotional", harmony_delta=1)
            $ arete_toast("Emotional", h=1)
            $ gs.adjust_trust("theo", +1)
            $ journal_add_today_event("Confided in Theo a little.", "Emotional +")
            th "Thanks. I’ll hold that gently."
        "Change the subject; ask about sticky tabs.":
            $ gs.arete.adjust("Psychological", harmony_delta=1)
            $ arete_toast("Psychological", h=1)
            $ gs.add_item("sticky_tabs")
            $ journal_add_today_event("Borrowed Theo’s rainbow sticky tabs.", "Psych +")
            th "Return them… eventually."

    $ bedtime = time_advance_and_check(55)
    if bedtime:
        jump go_to_bed
    jump day2_post_first

label day2_cas_arcade:
    $ set_flag("cas_met", True)
    $ gs.adjust_bond("cas", +1)
    scene black
    with dissolve
    cs "Field test volunteer! Perfect timing. I definitely did not break the token machine again."
    menu:
        "Offer to help test a cabinet.":
            $ gs.arete.adjust("Social", harmony_delta=1)
            $ arete_toast("Social", h=1)
            $ gs.adjust_trust("cas", +1)
            $ journal_add_today_event("Helped Cas test a suspicious cabinet.", "Social +")
            cs "Okay, if it starts smoking: photograph first, unplug second."
        "Ask what ‘ghost cabinet’ means.":
            $ gs.arete.adjust("Psychological", harmony_delta=1)
            $ arete_toast("Psychological", h=1)
            $ set_flag("CAS_SECRET_GHOST_CAB", True)
            $ journal_add_memory("cas", "There’s a cabinet that boots to a menu you can’t access without a special token.")
            $ journal_add_today_event("Cas slipped me a Ghost Cabinet Debug Token.", "Psych +")
            cs "It’s a rumor. Unless it isn’t. Here—debug token if you’re brave."
            $ gs.add_item("debug_token")
        "Insist on skee-ball first.":
            $ gs.arete.adjust("Physical", harmony_delta=1)
            $ arete_toast("Physical", h=1)
            $ journal_add_today_event("Skee-ball warmup before thinking too hard.", "Physical +")
            cs "Athlete. Fearsome."

    cs "Take some tokens. For science."
    $ gs.add_item("arcade_tokens")
    $ journal_add_today_event("Cas handed me five arcade tokens. ‘For science’.")
    $ bedtime = time_advance_and_check(50)
    if bedtime:
        jump go_to_bed
    jump day2_post_first

label day2_post_first:
    menu:
        "Do something else before night?"
        "Visit the other friend":
            if renpy.call_stack_depth() < 20:
                if get_flag("theo_met") and not get_flag("cas_met"):
                    jump day2_cas_arcade
                elif get_flag("cas_met") and not get_flag("theo_met"):
                    jump day2_theo_library
                else:
                    menu:
                        "Choose:"
                        "Library (Theo)":
                            jump day2_theo_library
                        "Arcade (Cas)":
                            jump day2_cas_arcade
        "Explore Town (free roam)":
            jump town_map
        "Call it a day (sleep)":
            jump go_to_bed

label day2_end:
    jump go_to_bed
