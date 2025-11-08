# helpers_toasts_combat.rpy — compatibility helpers (no combat logic yet)

init -20 python:
    # Legacy aliases many scripts expect:

    def set_flag(key, value=True):
        gs.set_flag(key, value)

    def spend_money(amount):
        # legacy wrapper
        return gs.spend(int(amount))

    def earn_money(amount):
        gs.earn(int(amount))

    # Relationship notifiers
    def bond_up(npc_id, delta=1):
        gs.adjust_bond(npc_id, int(delta))
        try:
            renpy.notify("+ Bond ({})".format(npc_id))
        except Exception:
            pass

    def trust_up(npc_id, delta=1):
        gs.adjust_trust(npc_id, int(delta))
        try:
            renpy.notify("+ Trust ({})".format(npc_id))
        except Exception:
            pass

    # Money notifiers
    def notify_cash(delta):
        if int(delta) >= 0:
            gs.earn(int(delta))
            renpy.notify("+${}".format(int(delta)))
        else:
            if gs.spend(-int(delta)):
                renpy.notify("-${}".format(-int(delta)))
            else:
                renpy.notify("Not enough cash.")
