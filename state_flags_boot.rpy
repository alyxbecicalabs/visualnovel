# state_flags_boot.rpy — FlagDict & safe seeding

init -1001 python:
    class FlagDict(dict):
        """
        Dict that never KeyErrors:
        - Unknown keys return False and are stored as False on first access.
        - Values are coerced to bool on set.
        """
        def __missing__(self, key):
            dict.__setitem__(self, key, False)
            return False
        def __setitem__(self, key, value):
            dict.__setitem__(self, key, bool(value))

    def _ensure_flagdict():
        try:
            if not isinstance(gs.flags, FlagDict):
                gs.flags = FlagDict(gs.flags)
        except Exception:
            pass

    # Convenience used at start of day/game
    def seed_missing_flags():
        _ensure_flagdict()
        required = [
            "day1_rowan_done",
            "day1_mina_done",
        ]
        for k in required:
            _ = gs.flags[k]  # touching seeds False if missing

    # Shorthand accessors
    def set_flag(name, value=True):
        _ensure_flagdict()
        gs.flags[name] = value

    def get_flag(name, default=False):
        _ensure_flagdict()
        try:
            val = gs.flags[name]  # will seed to False if missing
            return val if name in gs.flags else default
        except Exception:
            return default
