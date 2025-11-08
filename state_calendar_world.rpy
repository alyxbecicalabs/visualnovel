# state_calendar_world.rpy
# World weather & moon phase. Safe to call every morning.

init -1 python:
    import random

    class WorldState(object):
        def __init__(self):
            self.current_weather = "clear"
            self.moon_phase = "waxing"

        def pick_weather(self, season):
            pool = {
                "spring": ["clear","windy","drizzle","overcast"],
                "summer": ["clear","hot","humid","storm"],
                "autumn": ["clear","breezy","overcast","rain"],
                "winter": ["clear","snow","overcast","sleet"],
            }.get(season, ["clear","overcast"])
            return random.choice(pool)

        def roll_moon(self):
            return random.choice(["new","waxing","full","waning"])

        def new_day_roll(self):
            season = getattr(gs, "season", "spring")
            self.current_weather = self.pick_weather(season)
            self.moon_phase = self.roll_moon()

default world = WorldState()
