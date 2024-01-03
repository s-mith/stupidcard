#from events\subevents\eventZone.py import EventZone
#imports
class EventZonePlayer(EventZone):
    def __init__(self, id, gamemaster, owner, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner, effect_player):
        super().__init__(id, gamemaster, owner, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner)
        self.owner = effect_player