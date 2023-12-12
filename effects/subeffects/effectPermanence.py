from permanence import Permanence
from effect import Effect
from player import Player

class EffectPermanence(Effect):
    def __init__(self, effect: Effect, permanence: Permanence, permanence_owner: Player):
        super().__init__(effect)
        self.permanence = permanence
        self.permanence_owner = permanence_owner
        
        
