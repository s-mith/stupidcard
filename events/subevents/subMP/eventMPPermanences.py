from eventMP import EventMP
from player import Player
from permanence import Permanence

class EventMPCard(EventMP):
    def __init__(self, id, gamemaster, old_mp: int, new_mp: int, target_player: Player, effect_permanence_owner: Player, effect_permanence: Permanence):
        super().__init__(id, old_mp, new_mp, target_player)
        self.effect_permanence_owner = effect_permanence_owner
        self.effect_permanence = effect_permanence