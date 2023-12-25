#from events\subevents\eventZone.py import EventZone
#imports
class EventZonesPlayer(EventZone):
    def __init__(self, id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner, effect_player):
        super().__init__(id, gamemaster, None, old_zone, new_zone, old_zone_owner, new_zone_owner)
        self.owner = effect_player
        self.moving_card = moving_card
    def execute(self):
        if type(self.moving_card) == list:
            for card in self.moving_card:
                self.new_zone.add_card(self.old_zone.remove_card(card))
        else:
            self.new_zone.add_card(self.old_zone.remove_card(self.moving_card)) 