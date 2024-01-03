from eventHP import EventHP
from player import Player
from cardSpell import CardSpell

class EventHPSpell(EventHP):
    def __init__(self, id, gamemaster, owner, old_hp: int, new_hp: int, effect_card_owner: Player, effect_card: CardSpell):
        super().__init__(id, old_hp, new_hp)
        self.effect_card_owner = effect_card_owner
        self.effect_card = effect_card
        

