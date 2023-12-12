from card import Card
from effect import Effect
from player import Player

class EffectCard(Effect):
    def __init__(self, effect: Effect, card:Card, card_owner: Player):
        super().__init__(effect)
        self.card = card
        self.card_owner = card_owner
        
        
