# gui.rpy — simple, safe GUI bootstrap for Ren'Py 8.x

init offset = -2

init python:
    gui.init(1280, 720)

# Readable defaults
define gui.accent_color = "#ff2e97"
define gui.text_color = "#FFFFFF"
define gui.interface_text_color = "#FFFFFF"
define gui.name_text_color = "#FFFFFF"
define gui.idle_color = "#FFFFFF"
define gui.hover_color = "#FFFFFF"

define gui.text_size = 28
define gui.name_text_size = 36
define gui.interface_text_size = 24
define gui.label_text_size = 30
define gui.title_text_size = 42

define gui.window = "auto"
define gui.dialogue_text_xalign = 0.0

# Simple title style used by your custom screens
style menu_title is default
style menu_title:
    size 42
    color gui.text_color
    xalign 0.5
    outlines [(2, "#00000099", 0, 0)]
