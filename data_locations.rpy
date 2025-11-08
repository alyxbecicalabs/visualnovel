# data_locations.rpy — minimal, valid location catalog

init -1 python:
    LOCATIONS = {
        "coffee_shop": {
            "id": "coffee_shop",
            "name": "Blue Gull Coffee",
            "district": "Boardwalk",
            "type": "cafe",
            "desc": "Warm light, salt air, clack of cups.",
            "shop_id": "shop_coffee",
        },
        "boardwalk_rail": {
            "id": "boardwalk_rail",
            "name": "Boardwalk Rail",
            "district": "Boardwalk",
            "type": "hangout",
            "desc": "Your friends’ unofficial office; gulls file all complaints.",
            "shop_id": None,
        },
        "library": {
            "id": "library",
            "name": "Seafront Public Library",
            "district": "Old Town",
            "type": "library",
            "desc": "Quiet brick refuge. Dust motes have tenure.",
            "shop_id": "shop_library",
        },
        "library_arch": {
            "id": "library_arch",
            "name": "Archive Stacks",
            "district": "Old Town",
            "type": "archives",
            "desc": "Cool air, card catalog cards with secret lives.",
            "shop_id": None,
        },
        "arcade": {
            "id": "arcade",
            "name": "Night Harbor Arcade",
            "district": "Midway",
            "type": "arcade",
            "desc": "Neon hum; cabinets whisper myths when no one’s listening.",
            "shop_id": "shop_arcade",
        },
        "alley_stage": {
            "id": "alley_stage",
            "name": "Alley Stage",
            "district": "Backline",
            "type": "busk_spot",
            "desc": "Milk crate throne; the alley keeps time.",
            "shop_id": None,
        },
        "rooftop": {
            "id": "rooftop",
            "name": "Rooftop",
            "district": "Uptown",
            "type": "viewpoint",
            "desc": "The town in miniature, the wind reading your mind.",
            "shop_id": None,
        },
    }
