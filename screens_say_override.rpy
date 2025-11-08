# screens_say_override.rpy — clean, modern say screen

screen say(who, what):
    zorder 50
    window:
        id "window"

        has vbox

        if who is not None:
            text who id "who"

        text what id "what"
