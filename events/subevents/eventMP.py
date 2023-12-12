from event import Event
from player import Player
from gameMaster import GameMaster


class EventMP(Event):
    def __init__(self, id, gamemaster: GameMaster, old_mp: int, new_mp: int, target_player: Player):
        super().__init__(id, gamemaster)
        self.old_mp = old_mp
        self.new_mp = new_mp
        self.target_player = target_player
    
    def execute(self):
        self.target_player.set_mana(self.new_mp)
