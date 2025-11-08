# characters.rpy
# Speaker definitions with side images enabled for textbox portraits.

# Palette (tweak to your GUI)
define n_nyx  = "#CFE6FF"
define n_mina = "#FFD5EA"
define n_row  = "#D2FFD5"
define n_theo = "#FFE6B3"
define n_cas  = "#D4E8FF"
define n_jax  = "#FFF0C2"
define n_tal  = "#E3D5FF"
define n_sys  = "#FFFFFF"

define narr = Character(None, what_prefix="", what_suffix="")

# Main cast — `image="<tag>"` links to portrait/side images with that tag.
define ny = Character("Nyx",   image="nyx",   color=n_nyx,  show_side_image=True, who_outlines=[(2, "#00000080")])
define mn = Character("Mina",  image="mina",  color=n_mina, show_side_image=True, who_outlines=[(2, "#00000080")])
define rw = Character("Rowan", image="rowan", color=n_row,  show_side_image=True, who_outlines=[(2, "#00000080")])
define th = Character("Theo",  image="theo",  color=n_theo, show_side_image=True, who_outlines=[(2, "#00000080")])
define cs = Character("Cas",   image="cas",   color=n_cas,  show_side_image=True, who_outlines=[(2, "#00000080")])
define jx = Character("Jax",   image="jax",   color=n_jax,  show_side_image=True, who_outlines=[(2, "#00000080")])
define tl = Character("Talia", image="talia", color=n_tal,  show_side_image=True, who_outlines=[(2, "#00000080")])

define narr_sys = Character(" ", what_prefix="", what_suffix="", color=n_sys)
