from eventMP import EventMP
from player import Player


class EventMPCard(EventMP):
    def __init__(self, id, gamemaster, owner, old_mp: int, new_mp: int, target_player: Player, effect_player: Player):
        super().__init__(id, old_mp, new_mp, target_player)
        self.effect_player = effect_player
        