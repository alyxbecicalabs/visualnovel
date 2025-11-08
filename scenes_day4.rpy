# scenes_day4.rpy

label day4_entry:
    $ gs.set_time(4, "morning")
    $ world.new_day_roll()
    scene black
    with fade
    narr "Day 4. You catch yourself smiling before remembering to hide it."
    $ journal_add_today_event("Day 4 start. Weather: %s; Moon: %s." % (world.current_weather, world.moon_phase))

    menu:
        "Where first?"
        "Coffee Shop (Mina)":
            jump day4_mina_coffee
        "Boardwalk Rail (Rowan)":
            jump day4_rowan_rail
        "Explore Town (free roam)":
            jump town_map

label day4_mina_coffee:
    $ gs.adjust_bond("mina", +1)
    scene black
    with dissolve
    mn "I made something for you. Warning: it’s stapled and emotionally honest."
    $ gs.add_zine("brain_fog_survival")
    $ journal_add_today_event("Mina gave me her zine: ‘Brain Fog Survival Guide’.")
    menu:
        "Read a page with her.":
            $ gs.arete.adjust("Psychological", harmony_delta=1)
            $ arete_toast("Psychological", h=1)
            $ gs.adjust_trust("mina", +1)
            $ journal_add_today_event("Read a page together.", "Psych +")
            mn "You can annotate it. I won’t be mad."
        "Tuck it away for later, thank her.":
            $ gs.arete.adjust("Emotional", harmony_delta=1)
            $ arete_toast("Emotional", h=1)
            $ journal_add_today_event("Pocketed the zine respectfully.", "Emotional +")
            mn "You’re allowed to save soft things for later."

    menu:
        "Ask how she’s doing (really).":
            $ gs.arete.adjust("Social", harmony_delta=1)
            $ arete_toast("Social", h=1)
            $ journal_add_today_event("Checked in with Mina.", "Social +")
            mn "Not bad. Not good. Very—alive."
        "Offer to fetch water and actually do it.":
            $ gs.arete.adjust("Physical", harmony_delta=1)
            $ arete_toast("Physical", h=1)
            $ journal_add_today_event("Brought Mina a glass of water.", "Physical +")
            mn "Thanks. You’re good at the tiny logistics of care."

    $ bedtime = time_advance_and_check(55)
    if bedtime:
        jump go_to_bed
    jump day4_post_first

label day4_rowan_rail:
    $ gs.adjust_bond("rowan", +1)
    scene black
    with dissolve
    rw "Look at this. I made you a grip patch. Don’t ask how many I ruined first."
    $ gs.add_item("grip_patch")
    $ journal_add_today_event("Rowan gave me a grip tape patch.")
    menu:
        "Tell him the sunrise thing stuck with you.":
            $ gs.arete.adjust("Emotional", harmony_delta=1)
            $ arete_toast("Emotional", h=1)
            $ gs.adjust_trust("rowan", +1)
            $ journal_add_today_event("Revisited the sunrise thought.", "Emotional +")
            rw "I keep meaning it and unmeaning it. You know?"
        "Ask if he’ll teach you a basic trick.":
            $ gs.arete.adjust("Physical", harmony_delta=1)
            $ arete_toast("Physical", h=1)
            $ journal_add_today_event("Rowan started to teach a basic trick.", "Physical +")
            rw "Step one: do not become pavement."

    $ bedtime = time_advance_and_check(50)
    if bedtime:
        jump go_to_bed
    jump day4_post_first

label day4_post_first:
    menu:
        "Do something else before night?"
        "Visit the other friend":
            menu:
                "Choose:"
                "Coffee Shop (Mina)":
                    jump day4_mina_coffee
                "Boardwalk Rail (Rowan)":
                    jump day4_rowan_rail
        "Explore Town (free roam)":
            jump town_map
        "Call it a day (sleep)":
            jump go_to_bed

label day4_end:
    jump go_to_bed
