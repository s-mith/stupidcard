from event import Event
from player import Player
from card import Card
from gameMaster import GameMaster

class EventHP(Event):
    def __init__(self, id, gamemaster, owner: GameMaster, old_hp: int, new_hp: int):
        super().__init__(id)
        self.old_hp = old_hp
        self.new_hp = new_hp