# script.rpy — day flow & dream routing

label start:
    $ seed_missing_flags()
    $ world.new_day_roll()
    $ gs.hour = 8
    $ gs.minute = 0
    jump day1_entry

label go_to_bed:
    "You crash into bed. The day dissolves."
    call dream_entry
    $ gs.day_number += 1
    $ gs.hour = 8
    $ gs.minute = 0
    $ seed_missing_flags()
    $ world.new_day_roll()
    jump day_router

label dream_entry:
    call dream_stub
    return

label day_router:
    if gs.day_number == 1:
        jump day1_entry
    elif gs.day_number == 2:
        jump day2_entry
    elif gs.day_number == 3:
        jump day3_entry
    elif gs.day_number == 4:
        jump day4_entry
    elif gs.day_number == 5:
        jump day5_entry
    elif gs.day_number == 6:
        jump day6_entry
    else:
        jump day7_entry

label town_map:
    scene black
    with fade
    narr "You meander through town for a while."
    $ gs.advance_minutes(30)
    jump day_router
