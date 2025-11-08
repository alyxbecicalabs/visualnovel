# options.rpy (safe boot toggles)
define config.developer = True
define config.rollback_enabled = True

# IMPORTANT: don't auto-show any overlay screens at boot (main menu / splash).
init -2 python:
    config.overlay_screens = []   # we'll show HUD manually after the game starts
