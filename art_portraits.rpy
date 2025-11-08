# art_portraits.rpy
# VN-friendly portraits + transforms. 900x1600 PNGs align bottom.

# Images (use your working filenames)
image nyx base  = "images/characters/Tsukidere_Nyx.png"
image mina base = "images/characters/Tsukidere_Mina.png"

# Placeholders for other integrated NPCs (safe, invisible if shown by mistake).
# Replace with real files as you add them.
image rowan base = Solid("#0000")
image theo base  = Solid("#0000")
image cas base   = Solid("#0000")
image jax base   = Solid("#0000")
image talia base = Solid("#0000")

# Clean placements
transform vn_left:
    xalign 0.0
    yalign 1.0
    xoffset 80

transform vn_right:
    xalign 1.0
    yalign 1.0
    xoffset -80

transform vn_center:
    xalign 0.5
    yalign 1.0
