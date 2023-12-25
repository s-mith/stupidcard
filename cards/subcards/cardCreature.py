class CardCreature(Card):
    def __init__(self, name, cost, effects, text, id, gameid, attack, life):
        super().__init__(name, cost, effects, text, id, gameid)
        self.attack = attack
        self.life = life
    def set_life(self, life):
        self.life = life
    def is_creature(self):
        return True
    def is_spell(self):
        return False