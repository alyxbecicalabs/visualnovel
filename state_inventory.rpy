# state_inventory.rpy — robust helpers for items and zines

init -1 python:
    def add_item(item_id, qty=1):
        try:
            gs.add_item(item_id, qty)
        except Exception:
            gs.inventory[item_id] = gs.inventory.get(item_id, 0) + int(qty)

    def has_item(item_id, qty=1):
        return gs.inventory.get(item_id, 0) >= int(qty)

    def remove_item(item_id, qty=1):
        if has_item(item_id, qty):
            gs.inventory[item_id] -= int(qty)
            if gs.inventory[item_id] <= 0:
                del gs.inventory[item_id]
            return True
        return False

    def add_zine(z_id):
        if z_id not in gs.zine_inventory:
            gs.zine_inventory.append(z_id)

    def has_zine(z_id):
        return z_id in gs.zine_inventory
