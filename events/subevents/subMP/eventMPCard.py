from eventMP import EventMP
from card import Card
from player import Player

class EventMPCard(EventMP):
    def __init__(self, id, gamemaster, old_mp: int, new_mp: int, target_player: Player, effect_card_owner: Player, effect_card: Card):
        super().__init__(id, old_mp, new_mp, target_player)
        self.effect_card_owner = effect_card_owner
        self.effect_card = effect_card