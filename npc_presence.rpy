# npc_presence.rpy
# Utility to decide if an NPC is at a given location right now by schedule.

init -1 python:
    # Expect: gs.npcs[npc_id].schedule is a dict keyed by (dow, location_id)
    # with value list of (start_hour, end_hour) tuples.
    #
    # Example:
    # npc.schedule[(1, "CoffeeShop")] = [(8,12), (14,18)]
    #
    def npc_is_present(npc_id, loc_id):
        npcd = gs.npcs.get(npc_id)
        if not npcd:
            return False
        k = (gs.dow(), loc_id)
        blocks = getattr(npcd, "schedule", {}).get(k, [])
        h = gs.hour
        for start, end in blocks:
            if start <= h < end:
                return True
        return False
