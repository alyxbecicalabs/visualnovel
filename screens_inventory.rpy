# screens_inventory.rpy — stable inventory/zines viewer

screen inventory_screen():
    tag menu
    use game_menu(_("Inventory"), scroll=None):
        vbox:
            spacing 12
            text ("Cash: ${}".format(gs.cash))

            hbox:
                spacing 20

                frame:
                    style "menu_frame"
                    xsize 460
                    vbox:
                        spacing 6
                        text "Items" style "menu_title"

                        $ items = dict(getattr(gs, "inventory", {}))
                        if items:
                            viewport:
                                draggable True
                                mousewheel True
                                scrollbars "vertical"
                                ymaximum 520
                                vbox:
                                    for iid, count in sorted(items.items()):
                                        text "[iid]  ×[count]"
                        else:
                            text "No items."

                frame:
                    style "menu_frame"
                    xsize 460
                    vbox:
                        spacing 6
                        text "Zines" style "menu_title"

                        $ zines = list(getattr(gs, "zine_inventory", []))
                        if zines:
                            viewport:
                                draggable True
                                mousewheel True
                                scrollbars "vertical"
                                ymaximum 520
                                vbox:
                                    for zid in sorted(zines):
                                        text zid
                        else:
                            text "No zines."
