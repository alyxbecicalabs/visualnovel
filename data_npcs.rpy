# data_npcs.rpy — core NPC metadata & initializer

init -1 python:
    # Gift preferences keyed by npc_id
    GIFT_PREFERENCES = {
        "mina": {
            "love_tags": ["tea", "soft"],
            "like_tags": ["coffee", "pastry", "care"],
            "dislike_tags": ["token"],
            "love_items": ["brain_fog_survival", "woven_bracelet"],
            "like_items": [],
            "dislike_items": [],
        },
        "rowan": {
            "love_tags": ["book", "zine"],
            "like_tags": ["coffee"],
            "dislike_tags": [],
            "love_items": [],
            "like_items": [],
            "dislike_items": [],
        },
        "theo": {"love_tags": [], "like_tags": [], "dislike_tags": [], "love_items": [], "like_items": [], "dislike_items": []},
        "cas":  {"love_tags": [], "like_tags": [], "dislike_tags": [], "love_items": [], "like_items": [], "dislike_items": []},
        "jax":  {"love_tags": [], "like_tags": [], "dislike_tags": [], "love_items": [], "like_items": [], "dislike_items": []},
        "talia":{"love_tags": [], "like_tags": [], "dislike_tags": [], "love_items": [], "like_items": [], "dislike_items": []},
    }

    def init_core_npcs():
        from renpy.store import gs, Friend
        core = [
            ("mina", "Mina"),
            ("rowan", "Rowan"),
            ("theo", "Theo"),
            ("cas",  "Cas"),
            ("jax",  "Jax"),
            ("talia","Talia"),
        ]
        for fid, name in core:
            if fid not in gs.npcs:
                gs.npcs[fid] = Friend(fid, name)
