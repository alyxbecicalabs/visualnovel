# scenes_day3.rpy

label day3_entry:
    $ gs.set_time(3, "morning")
    $ world.new_day_roll()
    scene black
    with fade
    narr "Day 3. Your ribs feel like shelves holding rain."
    $ journal_add_today_event("Morning drift. Weather: %s; Moon: %s." % (world.current_weather, world.moon_phase))

    menu:
        "Where first?"
        "Alley Stage (Jax)":
            jump day3_jax_stage
        "Rooftop (Talia)":
            jump day3_talia_rooftop
        "Explore Town (free roam)":
            jump town_map

label day3_jax_stage:
    $ set_flag("jax_met", True)
    $ gs.adjust_bond("jax", +1)
    scene black
    with dissolve
    jx "Hey starghost. Want to hold the pick jar so it doesn’t run away?"
    menu:
        "Ask about the song he’s working on.":
            $ gs.arete.adjust("Emotional", harmony_delta=1)
            $ arete_toast("Emotional", h=1)
            $ gs.adjust_trust("jax", +1)
            $ journal_add_today_event("Listened to Jax play a not-quite-resolving loop.", "Emotional +")
            jx "It’s a loop that doesn’t resolve. That’s kind of the point."
        "Share a dumb rhyme.":
            $ gs.arete.adjust("Social", harmony_delta=1)
            $ arete_toast("Social", h=1)
            $ journal_add_today_event("Traded a rhyme with Jax.", "Social +")
            jx "Put that on the bridge. I’m stealing it."

    jx "Here. Lucky pick. It’s seen things."
    $ gs.add_item("guitar_pick")
    $ journal_add_today_event("Jax handed me his lucky blue guitar pick.")
    menu:
        "Ask why he busks here, specifically.":
            $ gs.arete.adjust("Psychological", harmony_delta=1)
            $ arete_toast("Psychological", h=1)
            $ set_flag("JAX_SECRET_RUN", True)
            $ journal_add_memory("jax", "He once ran from a bad scene, and this alley felt like a choice instead of a chase.")
            $ journal_add_today_event("Jax told me why this alley matters.", "Psych +")
            jx "It’s a promise to myself."
        "Nod; just listen.":
            $ gs.arete.adjust("Spiritual", harmony_delta=1)
            $ arete_toast("Spiritual", h=1)
            $ journal_add_today_event("Chose silence with music.", "Spiritual +")
            jx "Silence with witnesses is still music."

    $ bedtime = time_advance_and_check(50)
    if bedtime:
        jump go_to_bed
    jump day3_post_first

label day3_talia_rooftop:
    $ set_flag("talia_met", True)
    $ gs.adjust_bond("talia", +1)
    scene black
    with dissolve
    tl "Careful—loose gravel. Also hi."
    menu:
        "Ask how long she’s been awake.":
            $ gs.arete.adjust("Psychological", harmony_delta=1)
            $ arete_toast("Psychological", h=1)
            $ set_flag("TALIA_SECRET_NO_SLEEP", True)
            $ journal_add_memory("talia", "Sleep and she are not currently on speaking terms.")
            $ journal_add_today_event("We talked about sleep debt on the roof.", "Psych +")
            tl "Define ‘awake’."
        "Ask if you can borrow her spare flashlight.":
            $ gs.arete.adjust("Spiritual", harmony_delta=1)
            $ arete_toast("Spiritual", h=1)
            $ gs.add_item("mini_flashlight")
            $ journal_add_today_event("Talia lent me a mini flashlight with taped battery.", "Spiritual +")
            tl "Bring it back if it starts flickering; they do that."

    tl "There’s a pattern to the planes leaving. People don’t think to look."
    menu:
        "Try to spot it together.":
            $ gs.arete.adjust("Spiritual", harmony_delta=1)
            $ arete_toast("Spiritual", h=1)
            $ gs.adjust_trust("talia", +1)
            $ journal_add_today_event("Spotted a leaving-plane pattern with Talia.", "Spiritual +")
            tl "You saw it too."
        "Make a star joke to hide the ache.":
            $ gs.arete.adjust("Social", harmony_delta=1)
            $ arete_toast("Social", h=1)
            $ journal_add_today_event("Deflected with star humor. It still helped.", "Social +")
            tl "Comedy against entropy. Valid tactic."

    $ bedtime = time_advance_and_check(50)
    if bedtime:
        jump go_to_bed
    jump day3_post_first

label day3_post_first:
    menu:
        "Do something else before night?"
        "Visit the other friend":
            if get_flag("jax_met") and not get_flag("talia_met"):
                jump day3_talia_rooftop
            elif get_flag("talia_met") and not get_flag("jax_met"):
                jump day3_jax_stage
            else:
                menu:
                    "Choose:"
                    "Alley Stage (Jax)":
                        jump day3_jax_stage
                    "Rooftop (Talia)":
                        jump day3_talia_rooftop
        "Explore Town (free roam)":
            jump town_map
        "Call it a day (sleep)":
            jump go_to_bed

label day3_end:
    jump go_to_bed
