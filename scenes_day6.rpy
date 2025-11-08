# scenes_day6.rpy

label day6_entry:
    $ gs.set_time(6, "morning")
    $ world.new_day_roll()
    scene black
    with fade
    narr "Day 6. You breathe without counting it first."
    $ journal_add_today_event("Day 6 start. Weather: %s; Moon: %s." % (world.current_weather, world.moon_phase))

    menu:
        "Where first?"
        "Alley Stage (Jax) — loose jam":
            jump day6_jax_jam
        "Rooftop (Talia) — meteor whispers":
            jump day6_talia_meteors
        "Explore Town (free roam)":
            jump town_map

label day6_jax_jam:
    $ gs.adjust_bond("jax", +1)
    scene black
    with dissolve
    jx "Strum this with me. Down-stroke on the breath, up on the thought."
    menu:
        "Actually play a little.":
            $ gs.arete.adjust("Physical", harmony_delta=1)
            $ arete_toast("Physical", h=1)
            $ gs.adjust_trust("jax", +1)
            $ journal_add_today_event("Played a little with Jax. Messy good.", "Physical +")
            jx "See? You don’t have to be good to be part of it."
        "Just nod time with your foot.":
            $ gs.arete.adjust("Social", harmony_delta=1)
            $ arete_toast("Social", h=1)
            $ journal_add_today_event("Kept time while Jax riffed.", "Social +")
            jx "Bass player energy. Respect."

    $ gs.add_item("setlist_scrap")
    $ journal_add_today_event("Jax gave me a setlist scrap with chords + jokes.")
    $ bedtime = time_advance_and_check(45)
    if bedtime:
        jump go_to_bed
    jump day6_post_first

label day6_talia_meteors:
    $ gs.adjust_bond("talia", +1)
    scene black
    with dissolve
    tl "Meteor shower tonight. The sky’s going to shed glitter."
    menu:
        "Ask for a sketch of where to look.":
            $ gs.arete.adjust("Spiritual", harmony_delta=1)
            $ arete_toast("Spiritual", h=1)
            $ gs.adjust_trust("talia", +1)
            $ gs.add_item("star_chart_doodle")
            $ journal_add_today_event("Talia drew me a star chart doodle.", "Spiritual +")
        "Offer her tea later if she actually sleeps.":
            $ gs.arete.adjust("Emotional", harmony_delta=1)
            $ arete_toast("Emotional", h=1)
            $ journal_add_today_event("Offered post-meteor tea contingent on sleep.", "Emotional +")
            tl "Conditional kindness accepted."

    $ bedtime = time_advance_and_check(45)
    if bedtime:
        jump go_to_bed
    jump day6_post_first

label day6_post_first:
    menu:
        "Do something else before night?"
        "Visit the other friend":
            menu:
                "Choose:"
                "Alley Stage (Jax)":
                    jump day6_jax_jam
                "Rooftop (Talia)":
                    jump day6_talia_meteors
        "Explore Town (free roam)":
            jump town_map
        "Call it a day (sleep)":
            jump go_to_bed

label day6_end:
    jump go_to_bed
