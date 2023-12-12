from eventZone import EventZone
from card import Card
from zone import Zone
from player import Player


class EventZonePlayer(EventZone):
    def __itit__(self, id, gamemaster, moving_card:Card, old_zone:Zone, new_zone:Zone, old_zone_owner:Player, new_zone_owner:Player, effect_player: Player):
        super().__init__(id, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner)
        self.effect_player = effect_player

        

    


    


