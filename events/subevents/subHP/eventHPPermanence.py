from eventHP import EventHP
from player import Player
from permanence import Permanence

class EventHPPermanence(EventHP):
    def __init__(self, id, gamemaster, owner, old_hp: int, new_hp: int, effect_permanence_owner: Player, effect_permanence: Permanence):
        super().__init__(id, old_hp, new_hp)
        self.effect_permanence_owner = effect_permanence_owner
        self.effect_permanence = effect_permanence
        
        
