# scenes_day7.rpy

label day7_entry:
    $ gs.set_time(7, "morning")
    $ world.new_day_roll()
    scene black
    with fade
    narr "Day 7. End of the first loop. You feel less alone in your own echo."
    $ journal_add_today_event("Day 7 start. Weather: %s; Moon: %s." % (world.current_weather, world.moon_phase))

    menu:
        "Boardwalk day. Who do you drift toward first?"
        "Mina at the coffee cart":
            $ bedtime = time_advance_and_check(20)
            if bedtime:
                jump go_to_bed
            jump day7_mina
        "Rowan at the rail":
            $ bedtime = time_advance_and_check(20)
            if bedtime:
                jump go_to_bed
            jump day7_rowan
        "Theo near the library steps":
            $ bedtime = time_advance_and_check(20)
            if bedtime:
                jump go_to_bed
            jump day7_theo
        "Cas by the arcade doors":
            $ bedtime = time_advance_and_check(20)
            if bedtime:
                jump go_to_bed
            jump day7_cas
        "Jax tuning up":
            $ bedtime = time_advance_and_check(20)
            if bedtime:
                jump go_to_bed
            jump day7_jax
        "Talia frowning at the sky":
            $ bedtime = time_advance_and_check(20)
            if bedtime:
                jump go_to_bed
            jump day7_talia
        "Explore Town (free roam)":
            jump town_map

    menu:
        "Do anything else on the boardwalk?"
        "Visit someone else":
            jump day7_entry
        "Watch the water and call it a day":
            jump day7_end

label day7_mina:
    $ gs.adjust_bond("mina", +1)
    $ gs.arete.adjust("Emotional", harmony_delta=1)
    $ arete_toast("Emotional", h=1)
    mn "I made a tiny bracelet. Craft therapy works on Tuesdays and also today."
    $ gs.add_item("woven_bracelet")
    $ journal_add_today_event("Mina gave me a woven bracelet. Thread colors look familiar.", "Emotional +")
    return

label day7_rowan:
    $ gs.adjust_bond("rowan", +1)
    $ gs.arete.adjust("Social", harmony_delta=1)
    $ arete_toast("Social", h=1)
    rw "If we skate at sunrise tomorrow, it’s not an ending. It’s… an ongoing verb."
    $ journal_add_today_event("Shared a future-tense with Rowan.", "Social +")
    return

label day7_theo:
    $ gs.adjust_bond("theo", +1)
    $ gs.arete.adjust("Psychological", harmony_delta=1)
    $ arete_toast("Psychological", h=1)
    th "I found one of the names. Not all the way. Enough to keep looking."
    $ journal_add_today_event("Theo found a thread to pull on.", "Psych +")
    return

label day7_cas:
    $ gs.adjust_bond("cas", +1)
    $ gs.arete.adjust("Social", harmony_delta=1)
    $ arete_toast("Social", h=1)
    cs "If the cabinet blinks three times, it’s not my fault. It’s never my fault. It’s sometimes my fault."
    $ journal_add_today_event("Cas was very normal about blinking cabinets.", "Social +")
    return

label day7_jax:
    $ gs.adjust_bond("jax", +1)
    $ gs.arete.adjust("Emotional", harmony_delta=1)
    $ arete_toast("Emotional", h=1)
    jx "I wrote a second chord. It resolves if you believe in it."
    $ journal_add_today_event("Two-chord future with Jax.", "Emotional +")
    return

label day7_talia:
    $ gs.adjust_bond("talia", +1)
    $ gs.arete.adjust("Spiritual", harmony_delta=1)
    $ arete_toast("Spiritual", h=1)
    tl "Meteor glitter was late, but it arrived. I’m revising my thesis on patience."
    $ journal_add_today_event("Talia and I adjusted our patience model.", "Spiritual +")
    return

label day7_end:
    if gs.clock_minutes < 23*60+30:
        $ bedtime = time_advance_and_check(90)
        if bedtime:
            jump go_to_bed
    jump go_to_bed
