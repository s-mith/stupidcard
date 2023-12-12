from eventHPCeature import EventHPCreature
from player import Player
from cardCreature import CardCreature

class EventHPCreaturePlayer(EventHPCreature):
    def __init__(self, id, gamemaster, old_hp: int, new_hp: int, effect_card_owner: Player, effect_card: CardCreature, target_player: Player):
        super().__init__(id, old_hp, new_hp, effect_card_owner, effect_card)
        self.target_player = target_player




    def execute(self):
        self.target_player.set_life(self.new_hp)