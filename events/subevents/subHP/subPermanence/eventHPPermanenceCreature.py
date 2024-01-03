from eventHPPermanence import EventHPPermanence
from player import Player
from permanence import Permanence
from cardCreature import CardCreature

class EventHPPermanenceCreature(EventHPPermanence):
    def __init__(self, id, gamemaster, owner, old_hp: int, new_hp: int, effect_permanence_owner: Player, effect_permanence: Permanence, target_card_owner: Player, target_card: CardCreature):
        super().__init__(id, old_hp, new_hp, effect_permanence_owner, effect_permanence)
        self.target_card_owner = target_card_owner
        self.target_card = target_card


    def execute(self):
        self.target_card.set_life(self.new_hp)