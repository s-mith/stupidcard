from card import Card
from effect import Effect

class CardCreature(Card):
    def __init__(self, name:str, cost:int, effects:list[Effect], text:str, id:str, gameid:str, attack:int, life:int):
        super().__init__(name, cost, effects, text, id, gameid)
        self.attack = attack
        self.life = life

    def set_life(self, life):
        self.life = life

    def is_creature(self):
        return True
    
    def is_spell(self):
        return False

    