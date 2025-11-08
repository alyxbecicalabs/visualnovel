# state_flags.rpy — safe flags (no early gs access)

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
        """
        Convert gs.flags to FlagDict if gs exists and is loaded.
        Do nothing if gs isn't defined yet (default variables run after init).
        """
        try:
            from renpy.store import gs
        except Exception:
            return  # gs not ready during init scanning; that's fine.

        try:
            if not isinstance(gs.flags, FlagDict):
                gs.flags = FlagDict(gs.flags)
        except Exception:
            gs.flags = FlagDict()

    def seed_missing_flags(required=None):
        """
        Call this from label start (or new day) to guarantee required flags exist.
        """
        _ensure_flagdict()
        try:
            from renpy.store import gs
        except Exception:
            return
        req = required or [
            "day1_rowan_done",
            "day1_mina_done",
        ]
        for _k in req:
            gs.flags.setdefault(_k, False)

    def set_flag(name, value=True):
        _ensure_flagdict()
        try:
            from renpy.store import gs
            gs.flags[name] = bool(value)
        except Exception:
            pass

    def get_flag(name, default=False):
        _ensure_flagdict()
        try:
            from renpy.store import gs
            return bool(gs.flags.get(name, default))
        except Exception:
            return bool(default)
