class ZoneCard(Zone):
    def __init__(self, id):
        super().__init__(id)
        self.cards= []
    def size(self):
        return len(self.cards)
    def add_card(self, card):
        self.cards.append(card)
        return card
    def remove_card(self, card):
        self.cards.remove(card)
        return card
    def count(self):
        return len(self.cards)
    
