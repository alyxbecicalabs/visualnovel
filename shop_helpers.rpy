# shop_helpers.rpy — stock & access helpers

init -5 python:
    # Define ITEMS once if not defined elsewhere
    if "ITEMS" not in globals():
        ITEMS = {
            "coffee":      {"name": "Coffee", "price": 4,  "tags": ["coffee", "drink"]},
            "tea":         {"name": "Tea",    "price": 4,  "tags": ["tea", "drink", "soft"]},
            "pastry":      {"name": "Pastry", "price": 5,  "tags": ["pastry", "food"]},
            "zine_map":    {"name": "Zine: Map of Town", "price": 0, "tags": ["zine", "map"]},
            "arcade_token":{"name": "Arcade Token", "price": 2, "tags": ["token"]},
            "brain_fog_survival": {"name":"Brain Fog Survival", "price": 0, "tags":["zine","care"]},
            "woven_bracelet":     {"name":"Woven Bracelet", "price": 0, "tags":["soft"]},
        }

    if "SHOP_STOCKS" not in globals():
        SHOP_STOCKS = {
            "shop_coffee":  ["coffee", "tea", "pastry"],
            "shop_library": ["zine_map", "brain_fog_survival"],
            "shop_arcade":  ["arcade_token"],
        }

    def get_shop_inventory(shop_id):
        ids = SHOP_STOCKS.get(shop_id, [])
        inv = {}
        for iid in ids:
            meta = ITEMS.get(iid)
            if meta:
                inv[iid] = dict(meta)
        return inv
