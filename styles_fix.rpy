# styles_fix.rpy — define any styles that were missing from journal or menus.

# Provide a generic menu_title so journal/About don't crash.
style menu_title is default
style menu_title:
    size 48
    color "#FFFFFF"
    xalign 0.5
    outlines [(2,"#00000099",0,0)]

# Provide a small helper style for captions/subtitles if needed.
style small_caption is default
style small_caption:
    size 22
    color "#DDDDDD"
