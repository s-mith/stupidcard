class ZoneCardGraveyard(ZoneCard):
    def __init__(self, id):
        super().__init__(id)
    def get_top(self):
        return self.cards[0]
    def get_top_creature(self):
        for card in self.cards:
            if card.is_creature():
                return card
        return None
    def get_top_spell(self):
        for card in self.cards:
            if card.is_spell():
                return card
        return None