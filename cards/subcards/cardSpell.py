class CardSpell(Card):
    def __init__(self, name, cost, effects, text, id, gameid):
        super().__init__(name, cost, effects, text, id, gameid)
    def is_creature(self):
        return False
    def is_spell(self):
        return True