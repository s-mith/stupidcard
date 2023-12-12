from card import Card
from effect import Effect

class CardSpell(Card):
    def __init__(self, name:str, cost:int, effects:list[Effect], text:str, id:str, gameid:str):
        super().__init__(name, cost, effects, text, id, gameid)


    def is_creature(self):
        return False
    
    def is_spell(self):
        return True