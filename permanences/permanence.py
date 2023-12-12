from player import Player
from gameMaster import GameMaster
from effect import Effect

class Permanence:
    def __init__(self, effect: Effect, owner:Player):
        self.effect = effect
        self.owner = owner
        