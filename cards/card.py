# a card is an object that has a cost, name, and functions that are called whenever a action happens
from effect import Effect
from gameMaster import GameMaster

class Card:
    def __init__(self, name:str, cost:int, effects:list[Effect], text:str, id:str, gameid:str) -> None:
        self.name = name
        self.cost = cost
        self.effects = effects
        self.text = text
        self.id = id
        self.gameid = gameid

    def execute_effects(self, gamemaster: GameMaster) -> list[Effect]:
        # execute_effects 
        _effects:list[Effect] = []
        for effect in self.effects:
            x = effect.execute(gamemaster)
            _effects.append(x) if x != None else None
        return _effects


    
    def is_creature(self) -> bool:
        return False
    
    def is_spell(self) -> bool:
        return False
    
    