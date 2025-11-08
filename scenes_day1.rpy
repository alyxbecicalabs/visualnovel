# scenes_day1.rpy

label day1_entry:
    $ gs.set_time(1, "morning")
    $ world.new_day_roll()
    scene black
    with fade
    narr "Morning, Day 1."
    narr "You wake with that half-memory taste in your mouth—like someone said your name from far away."
    $ journal_add_today_event("Woke up feeling off. Weather: %s; Moon: %s." % (world.current_weather, world.moon_phase))
    $ journal_set_summary(1, "First day I actually tried to leave the room.")

    menu:
        "Where do you go this morning?"
        "Coffee Shop (see Mina)":
            jump day1_mina_coffee
        "Boardwalk Rail (find Rowan)":
            jump day1_rowan_rail
        "Explore Town (free roam)":
            jump town_map

label day1_mina_coffee:
    $ set_flag("mina_met", True)
    $ gs.flags["day1_mina_done"] = True
    $ gs.adjust_trust("mina", +1)
    $ gs.adjust_bond("mina", +1)
    scene black
    with dissolve
    mn "Morning. You look like regret before caffeine. What can I get you?"

    menu:
        "Ask for black coffee with gallows humor.":
            $ gs.arete.adjust("Emotional", harmony_delta=0, strife_delta=1)
            $ arete_toast("Emotional", s=1)
            $ gs.adjust_bond("mina", +1)
            $ journal_add_today_event("Ordered black coffee and joked too darkly.", "Emotional –")
            mn "Not my favorite order name, but sure. Try not to combust."
        "Ask for chamomile; you want to calm down.":
            $ gs.arete.adjust("Emotional", harmony_delta=1, strife_delta=0)
            $ arete_toast("Emotional", h=1)
            $ gs.adjust_trust("mina", +1)
            $ journal_add_today_event("Chose chamomile instead of panic-fuel.", "Emotional +")
            mn "Bold move before noon. I approve."
        "Ask her to surprise you (keep it mild).":
            $ gs.arete.adjust("Social", harmony_delta=1)
            $ arete_toast("Social", h=1)
            $ gs.adjust_bond("mina", +1)
            $ journal_add_today_event("Let Mina pick; it felt collaborative.", "Social +")
            mn "I'll keep it kind to your nervous system."

    mn "Joking aside... you're okay enough to sit? I can take my break."

    menu:
        "“Yeah. We can spiral in stereo.” {i}(open up a little){/i}":
            $ gs.arete.adjust("Emotional", harmony_delta=1)
            $ arete_toast("Emotional", h=1)
            $ gs.adjust_trust("mina", +1)
            $ set_flag("MINA_SECRET_LISTS", True)
            $ journal_add_today_event("Mina admitted she writes lists during brain-chew days.", "Psych +")
            $ journal_add_memory("mina", "She keeps ‘haven’t failed yet’ lists when her mind spirals.")
            mn "Nosy question back-and-forth? Deal. When my brain chews itself, I make lists—people I haven’t failed yet, things I haven’t ruined..."
        "“Can we keep it light today?”":
            $ gs.arete.adjust("Social", harmony_delta=1)
            $ arete_toast("Social", h=1)
            $ gs.adjust_bond("mina", +1)
            $ journal_add_today_event("Kept it light with Mina today.", "Social +")
            mn "Light it is. Tea tastes like warm grass anyway."
        "“I’m not up for questions.”":
            $ gs.arete.adjust("Emotional", harmony_delta=1)
            $ arete_toast("Emotional", h=1)
            $ journal_add_today_event("Set a boundary with Mina.", "Emotional +")
            mn "Boundaries accepted. We can just sit."

    $ journal_add_today_event("Talked with Mina at the coffee shop.")
    $ bedtime = time_advance_and_check(60)
    if bedtime:
        jump go_to_bed

    if gs.flags["day1_rowan_done"]:
        jump day1_end
    else:
        menu:
            "Do something else before night?"
            "Go to Boardwalk Rail (Rowan)":
                jump day1_rowan_rail
            "Explore Town (free roam)":
                jump town_map
            "Call it a day (sleep)":
                jump go_to_bed

label day1_rowan_rail:
    $ set_flag("rowan_met", True)
    $ gs.flags["day1_rowan_done"] = True
    scene black
    with dissolve
    rw "Hey. You look like sleep owes you money."

    menu:
        "Deflect with teasing. “You look like you fought the pavement and lost.”":
            $ gs.arete.adjust("Social", harmony_delta=1)
            $ arete_toast("Social", h=1)
            $ gs.adjust_bond("rowan", +1)
            $ journal_add_today_event("Bantered with Rowan.", "Social +")
            rw "Rude. I won."
        "Be honest. “I don’t want to be alone right now.”":
            $ gs.arete.adjust("Emotional", harmony_delta=1)
            $ arete_toast("Emotional", h=1)
            $ gs.adjust_bond("rowan", +1)
            $ gs.adjust_trust("rowan", +1)
            $ journal_add_today_event("Admitted you didn’t want to be alone with Rowan.", "Emotional +")
            rw "Sit. We can judge tourists in silence."
        "Set a boundary. “Please don’t call me nightmare girl.”":
            $ gs.arete.adjust("Emotional", harmony_delta=1)
            $ arete_toast("Emotional", h=1)
            $ gs.adjust_trust("rowan", +1)
            $ journal_add_today_event("Asked Rowan for gentler language.", "Emotional +")
            rw "Got it. Nyx, then. Hi."

    rw "You sticking around or doing a flyby?"

    menu:
        "Stick around and actually talk a bit.":
            $ gs.arete.adjust("Social", harmony_delta=1)
            $ arete_toast("Social", h=1)
            $ gs.adjust_bond("rowan", +1)
            $ journal_add_today_event("Stayed to actually talk to Rowan.", "Social +")
            rw "Payment is one bad joke per hour. Up front."
        "Open a window for a secret.":
            $ gs.arete.adjust("Emotional", harmony_delta=1)
            $ arete_toast("Emotional", h=1)
            $ set_flag("ROWAN_SECRET_SUNRISE_PLAN", True)
            $ gs.adjust_trust("rowan", +1)
            $ gs.adjust_bond("rowan", +1)
            $ journal_add_memory("rowan", "He sometimes dreams of skating off the island at sunrise—an escape, not a death wish.")
            $ journal_add_today_event("Rowan shared a sunrise thought.", "Emotional +")
            rw "Ssh. Don’t tell anyone: I keep thinking I’ll skate off this island at sunrise one day. Dramatic, right?"
        "Keep it light; watch the crowd.":
            $ gs.arete.adjust("Spiritual", harmony_delta=1)
            $ arete_toast("Spiritual", h=1)
            $ journal_add_today_event("Let the crowd become white noise with Rowan.", "Spiritual +")
            rw "Cursed boardwalk food tier list: everything ‘world’s hottest’ sits in S-tier for regret."

    $ journal_add_today_event("Watched the water with Rowan at the rail.")
    $ bedtime = time_advance_and_check(60)
    if bedtime:
        jump go_to_bed

    if gs.flags["day1_mina_done"]:
        jump day1_end
    else:
        menu:
            "Do something else before night?"
            "Go to Coffee Shop (Mina)":
                jump day1_mina_coffee
            "Explore Town (free roam)":
                jump town_map
            "Call it a day (sleep)":
                jump go_to_bed

label day1_end:
    if gs.clock_minutes < 23*60+30:
        $ bedtime = time_advance_and_check(90)
        if bedtime:
            jump go_to_bed
    jump go_to_bed
