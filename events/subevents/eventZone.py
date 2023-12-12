from event import Event
from zoneCard import ZoneCard
from card import Card
from player import Player
from gameMaster import GameMaster

class EventZone(Event):
    def __init__(self, id, gamemaster: GameMaster, moving_card:Card, old_zone:ZoneCard, new_zone:ZoneCard, old_zone_owner:Player, new_zone_owner:Player):
        super().__init__(id, gamemaster)
        self.moving_card = moving_card
        self.old_zone = old_zone
        self.new_zone = new_zone
        self.old_zone_owner = old_zone_owner
        self.new_zone_owner = new_zone_owner

        
    def execute(self):
        self.new_zone.add_card(self.old_zone.remove_card(self.moving_card))

    