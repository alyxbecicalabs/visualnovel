# data_items_zines.rpy — Items, zines, prices, tags, and per-location shop stocks.

init -3 python:
    ITEMS = {
        # Cafe
        "coffee_black":      {"name":"Black Coffee",            "type":"consumable","price":4, "giftable":True,  "tags":["coffee"]},
        "tea_chamomile":     {"name":"Chamomile Tea",           "type":"consumable","price":4, "giftable":True,  "tags":["tea","calm"]},
        "pastry_scone":      {"name":"Blueberry Scone",         "type":"consumable","price":3, "giftable":True,  "tags":["pastry","food"]},
        "woven_bracelet":    {"name":"Woven Bracelet",          "type":"trinket",  "price":0, "giftable":True,  "tags":["trinket","handmade","soft"]},

        # Pizza
        "brothers_slice":    {"name":"Slice of Pizza",          "type":"consumable","price":5, "giftable":True,  "tags":["food"]},

        # Library
        "archivist_bookmark":{"name":"Archivist’s Bookmark",    "type":"trinket",  "price":2, "giftable":True,  "tags":["books","archive","trinket"]},
        "sticky_tabs":       {"name":"Sticky Tabs",             "type":"utility",  "price":2, "giftable":True,  "tags":["books","study"]},
        "library_guest_pass":{"name":"Library Guest Pass",      "type":"key",      "price":0, "giftable":False, "tags":["key"]},

        # Arcade
        "arcade_tokens":     {"name":"Arcade Tokens (x5)",      "type":"pack",     "price":2, "giftable":False, "tags":["token","arcade"]},
        "debug_token":       {"name":"Ghost Debug Token",       "type":"key",      "price":0, "giftable":False, "tags":["token","arcade","weird"]},

        # Jax / music
        "guitar_pick":       {"name":"Lucky Guitar Pick",       "type":"trinket",  "price":0, "giftable":True,  "tags":["music","trinket"]},
        "setlist_scrap":     {"name":"Setlist Scrap",           "type":"trinket",  "price":0, "giftable":True,  "tags":["music","paper"]},

        # Talia / sky
        "mini_flashlight":   {"name":"Mini Flashlight",         "type":"utility",  "price":6, "giftable":True,  "tags":["stars","utility"]},
        "star_chart_doodle": {"name":"Star Chart Doodle",       "type":"trinket",  "price":0, "giftable":True,  "tags":["stars","trinket"]},

        # Rowan / skate
        "grip_patch":        {"name":"Grip Tape Patch",         "type":"trinket",  "price":0, "giftable":True,  "tags":["skate","trinket"]},

        # Zines
        "brain_fog_survival":{"name":"Zine: Brain Fog Survival","type":"zine",     "price":0, "giftable":True,  "tags":["zine","soft","care"]},
    }

    SHOP_STOCKS = {
        "shop_coffee": ["coffee_black","tea_chamomile","pastry_scone"],
        "shop_pizza":  ["brothers_slice"],
        "shop_library":["archivist_bookmark","sticky_tabs","mini_flashlight"],
        "shop_arcade": ["arcade_tokens"],
    }

# If another module hasn't provided this, define a dict-returning helper.
init -2 python:
    if "get_shop_inventory" not in globals():
        def get_shop_inventory(shop_id):
            ids = SHOP_STOCKS.get(shop_id, [])
            return {iid: dict(ITEMS[iid]) for iid in ids if iid in ITEMS}
