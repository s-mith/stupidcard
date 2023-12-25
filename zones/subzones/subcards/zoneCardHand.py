class ZoneCardHand(ZoneCard):
    def __init__(self, id,max_size):
        super().__init__(id)
        self.max_size = max_size
    def get_random_n(self, n):
        if n > self.size():
            return random.sample(self.cards, self.size())
        return random.sample(self.cards, n)