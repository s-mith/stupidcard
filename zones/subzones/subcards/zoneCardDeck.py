class ZoneCardDeck(ZoneCard):
    def __init__(self, id, cards):
        super().__init__(id)
        self.cards = cards
    def shuffle(self):
        tempdeck = []
        while len(self.cards) > 0:
            randindex = random.randint(0, len(self.cards) - 1)
            tempdeck.append(self.cards[randindex])
            self.cards.pop(randindex)
        self.cards = tempdeck
    def get_top(self):
        return self.cards[0]
    def get_n_top(self, n):
        return self.cards[n]
    def get_top_x(self, x):
        if x > self.size():
            return self.cards
        return self.cards[:x]
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