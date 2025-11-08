# fearform_cards.rpy — minimal, valid placeholders

init -1 python:
    class Card(object):
        def __init__(self, cid, name, domain_color, top, right, bottom, left, arcana_type="Minor"):
            self.id = cid
            self.name = name
            self.domain_color = domain_color
            self.top = top; self.right = right; self.bottom = bottom; self.left = left
            self.arcana_type = arcana_type

    class Deck(object):
        def __init__(self, cards=None):
            self.cards = list(cards or [])

    STARTER_CARDS = {}
