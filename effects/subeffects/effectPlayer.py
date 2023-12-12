from effect import Effect
from player import Player

class EffectPlayer(Effect):
    def __init__(self,id ,  effect: Effect, player: Player):
        super().__init__(id, effect)
        self.player = player
