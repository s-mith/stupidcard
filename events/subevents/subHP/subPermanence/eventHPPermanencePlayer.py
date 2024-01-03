from eventHPPermanence import EventHPPermanence
from player import Player
from permanence import Permanence

class EventHPPermanencePlayer(EventHPPermanence):
    def __init__(self, id, gamemaster, owner, old_hp: int, new_hp: int, effect_permanence_owner: Player, effect_permanence: Permanence, target_player: Player):
        super().__init__(id, old_hp, new_hp, effect_permanence_owner, effect_permanence)
        self.target_player = target_player
        
    def execute(self):    
        self.target_player.set_life(self.new_hp)