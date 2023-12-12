from eventHPSpell import EventHPSpell
from player import Player
from cardSpell import CardSpell

class EventHPSpellPlayer(EventHPSpell):
    def __init__(self, id, gamemaster, old_hp: int, new_hp: int, effect_spell_owner: Player, effect_spell: CardSpell, target_player: Player):
        super().__init__(id, old_hp, new_hp, effect_spell_owner, effect_spell)
        self.target_player = target_player
        
    def execute(self):
        self.target_player.set_life(self.new_hp)  
        