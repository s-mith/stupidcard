from eventHPSpell import EventHPSpell
from player import Player
from cardSpell import CardSpell
from cardCreature import CardCreature

class EventHPSpellCreature(EventHPSpell):
    def __init__(self, id, gamemaster, owner, old_hp: int, new_hp: int, effect_spell_owner: Player, effect_spell: CardSpell, target_card_owner: Player, target_card: CardCreature):
        super().__init__(id, old_hp, new_hp, effect_spell_owner, effect_spell)
        self.target_card_owner = target_card_owner
        self.target_card = target_card
        
    def execute(self):
        self.target_card.set_life(self.new_hp)