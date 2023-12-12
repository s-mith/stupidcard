from gameMaster import GameMaster
from event import Event
class Effect:
    def __init__(self,id, effect:function):
        self.id = id
        self.effect = effect

    def execute(self, gamemaster:GameMaster):  
        return self.effect(gamemaster)