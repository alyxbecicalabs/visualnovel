# stability_patch.rpy — safe fallbacks so content oopsies don’t crash the game.
# All helpers are guarded and only activate if your project didn’t define them.

init -200 python:
    # ---- WORLD ROLLS ----
    class _WorldFallback(object):
        def new_day_roll(self):
            # No-op if you haven't wired world RNG yet.
            return

    # Only create if world isn't present
    if "world" not in globals():
        world = _WorldFallback()

    # ---- JOURNAL ----
    class _JournalFallback(object):
        def __init__(self):
            self.day_log = {}  # {day_number: {"summary": str, "events": [str,...]}}

    if "journal" not in globals():
        journal = _JournalFallback()

    # Safe event-adder used across UIs/screens; only define if not provided by your journal module.
    if "journal_add_today_event" not in globals():
        def journal_add_today_event(msg):
            try:
                d = journal.day_log.setdefault(gs.day_number, {"summary": "", "events": []})
                d["events"].append(str(msg))
            except Exception:
                # If gs is unavailable for some reason, just ignore instead of crashing.
                pass

    # ---- SHOP INVENTORY NORMALIZER ----
    # If someone else doesn't define get_shop_inventory, provide a simple dict-based one.
    if "get_shop_inventory" not in globals():
        ITEMS = {
            "coffee_black":   {"name":"Black Coffee", "type":"consumable","price":4, "tags":["coffee"]},
            "tea_chamomile":  {"name":"Chamomile Tea","type":"consumable","price":4, "tags":["tea","calm"]},
        }
        SHOP_STOCKS = {"shop_coffee": ["coffee_black","tea_chamomile"]}
        def get_shop_inventory(shop_id):
            ids = SHOP_STOCKS.get(shop_id, [])
            return {iid: dict(ITEMS[iid]) for iid in ids if iid in ITEMS}

# ---- Missing Image Fallback ----
# Prevents hard crashes when a scene references an image you haven't imported yet.
init -5 python:
    def _tsuki_missing_image(*args, **kwargs):
        # Keep it simple and unobtrusive: a neutral solid.
        return Solid("#333333")
    # Only set if someone else hasn't already customized it.
    if getattr(config, "missing_image_callback", None) is None:
        config.missing_image_callback = _tsuki_missing_image
