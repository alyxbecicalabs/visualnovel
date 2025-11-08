# screens_shops.rpy — robust shop UI (accepts dict OR list-of-tuples inventories)

screen shop_screen(shop_id):
    modal True
    zorder 200
    default inv_raw = get_shop_inventory(shop_id)

    # Normalize to a dict: {item_id: meta}
    $ inv = inv_raw if isinstance(inv_raw, dict) else {iid: meta for (iid, meta) in (inv_raw or [])}

    frame:
        padding 15
        xalign 0.5
        yalign 0.5
        has vbox

        text ("Shop — " + shop_id) size 28
        text ("Cash: $" + str(gs.cash)) size 20

        if inv:
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                ymaximum 520
                vbox:
                    spacing 8
                    for iid, meta in sorted(inv.items()):
                        hbox:
                            spacing 12
                            text meta.get("name", iid)
                            text "$" + str(int(meta.get("price", 0)))
                            null width 20
                            textbutton "Buy":
                                action Function(_shop_buy, iid, inv)

        textbutton "Close" action Return(None) xalign 1.0

init -1 python:
    def _shop_buy(item_id, inv):
        from renpy.store import journal_add_today_event
        meta = inv.get(item_id, {})
        price = int(meta.get("price", 0))

        if price <= 0 or gs.spend(price):
            gs.add_item(item_id, 1)
            try:
                journal_add_today_event("Bought " + meta.get("name", item_id))
            except Exception:
                pass
            renpy.notify("Purchased.")
        else:
            renpy.notify("Not enough cash.")
