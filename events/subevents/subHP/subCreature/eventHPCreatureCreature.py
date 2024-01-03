from eventHPCeature import EventHPCreature
from player import Player
from cardCreature import CardCreature

class EventHPCreatureCreature(EventHPCreature):
    def __init__(self, id, gamemaster, owner, old_hp: int, new_hp: int, effect_card_owner: Player, effect_card: CardCreature, target_card_owner: Player, target_card: CardCreature):
        super().__init__(id, old_hp, new_hp, effect_card_owner, effect_card)
        self.target_card_owner = target_card_owner
        self.target_card = target_card




    def execute(self):
        self.target_card.set_life(self.new_hp)