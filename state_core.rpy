# state_core.rpy — core game state (time, money, flags, relationships, arete)

init -10 python:
    class Friend(object):
        def __init__(self, fid, name=None):
            self.id = fid
            self.name = name or fid
            self.bond = 0
            self.trust = 0
            self.schedule = {}  # optional: (dow, loc) -> [(start,end), ...]

    class AreteState(object):
        def __init__(self):
            # Pre-populate commonly used domains, but also accept new ones on the fly.
            self.domains = {
                "Emotional":      {"harmony": 0, "strife": 0},
                "Social":         {"harmony": 0, "strife": 0},
                "Physical":       {"harmony": 0, "strife": 0},
                "Psychological":  {"harmony": 0, "strife": 0},
                "Spiritual":      {"harmony": 0, "strife": 0},
                "Body":           {"harmony": 0, "strife": 0},
                "Mind":           {"harmony": 0, "strife": 0},
                "Will":           {"harmony": 0, "strife": 0},
            }

        def _bucket(self, domain):
            return self.domains.setdefault(domain, {"harmony": 0, "strife": 0})

        def add(self, domain, harmony=0, strife=0):
            d = self._bucket(domain)
            d["harmony"] += int(harmony)
            d["strife"]  += int(strife)

        # Scenes often call adjust(domain, harmony_delta=?, strife_delta=?)
        # Make this flexible and compatible with both styles.
        def adjust(self, domain, harmony_delta=0, strife_delta=0, harmony=None, strife=None, h=None, s=None):
            # Accept multiple kw variants without throwing.
            if harmony is not None:      harmony_delta = harmony
            if strife is not None:       strife_delta = strife
            if h is not None:            harmony_delta = h
            if s is not None:            strife_delta  = s
            self.add(domain, harmony=int(harmony_delta), strife=int(strife_delta))

    class GameState(object):
        def __init__(self):
            # Day/time
            self.day_number = 1
            self._time_minutes = 8 * 60  # 08:00 start
            self.time_segment = "morning"

            # Economy
            self.cash = 40

            # Flags and NPCs
            self.flags = {}
            self.npcs = {}

            # Arete + inventories
            self.arete = AreteState()
            self.inventory = {}      # item_id -> count
            self.zine_inventory = [] # list of zine ids

            # Calendar-ish helpers
            self.season = "spring"

        # ---------- TIME ----------
        def set_time(self, day, segment):
            self.day_number = int(day)
            mapping = {
                "morning":   8 * 60,
                "noon":     12 * 60,
                "afternoon":15 * 60,
                "evening":  19 * 60,
                "night":    22 * 60,
            }
            self._time_minutes = mapping.get(str(segment).lower(), 8 * 60)
            self.time_segment  = str(segment).lower()

        def get_time_segment(self):
            if getattr(self, "time_segment", None) in ("dream",):
                return self.time_segment
            m = self._time_minutes
            if   6*60 <= m < 12*60:  return "morning"
            elif 12*60 <= m < 17*60: return "afternoon"
            elif 17*60 <= m < 21*60: return "evening"
            elif 21*60 <= m or m < 6*60: return "night"
            else: return "day"

        def time_str(self):
            h = int(self._time_minutes // 60)
            mm = int(self._time_minutes % 60)
            return f"{h:02d}:{mm:02d}"

        def advance_minutes(self, mins):
            self._time_minutes = max(0, min(23*60+59, self._time_minutes + int(mins)))

        def set_clock(self, hour, minute):
            hour = max(0, min(23, int(hour)))
            minute = max(0, min(59, int(minute)))
            self._time_minutes = hour * 60 + minute

        def advance_day(self, days=1):
            self.day_number += int(days)
            self.set_clock(8, 0)
            self.time_segment = "morning"

        def need_bedtime(self):
            return self._time_minutes >= (22 * 60 + 30)

        @property
        def hour(self):
            return int(self._time_minutes // 60)

        @hour.setter
        def hour(self, h):
            m = self._time_minutes % 60
            self._time_minutes = max(0, min(23, int(h))) * 60 + m

        @property
        def minute(self):
            return int(self._time_minutes % 60)

        @minute.setter
        def minute(self, m):
            h = self._time_minutes // 60
            self._time_minutes = h * 60 + max(0, min(59, int(m)))

        @property
        def clock_minutes(self):
            return int(self._time_minutes)

        def dow(self):
            return ((self.day_number - 1) % 7) + 1  # 1..7

        def shop_minutes(self):
            return 10

        # ---------- ECON ----------
        def spend(self, amount):
            amount = int(amount)
            if amount <= 0:
                return True
            if self.cash >= amount:
                self.cash -= amount
                return True
            return False

        def earn(self, amount):
            self.cash += int(amount)

        # ---------- RELATIONSHIPS ----------
        def _get_friend(self, fid, name=None):
            f = self.npcs.get(fid)
            if f is None:
                f = Friend(fid, name)
                self.npcs[fid] = f
            return f

        def adjust_bond(self, fid, delta):
            self._get_friend(fid).bond += int(delta)

        def adjust_trust(self, fid, delta):
            self._get_friend(fid).trust += int(delta)

        # ---------- INVENTORY / ZINES ----------
        def add_item(self, item_id, qty=1):
            self.inventory[item_id] = self.inventory.get(item_id, 0) + int(qty)

        def has_item(self, item_id, qty=1):
            return self.inventory.get(item_id, 0) >= int(qty)

        def remove_item(self, item_id, qty=1):
            q = int(qty)
            if self.has_item(item_id, q):
                self.inventory[item_id] -= q
                if self.inventory[item_id] <= 0:
                    self.inventory.pop(item_id, None)
                return True
            return False

        def add_zine(self, z_id):
            if z_id not in self.zine_inventory:
                self.zine_inventory.append(z_id)

        def has_zine(self, z_id):
            return z_id in self.zine_inventory

        # ---------- FLAGS ----------
        def set_flag(self, name, value=True):
            self.flags[name] = bool(value)

# Global state
default gs = GameState()

init -9 python:
    def time_advance_and_check(mins):
        try:
            gs.advance_minutes(int(mins))
            return gs.need_bedtime()
        except Exception:
            return False
