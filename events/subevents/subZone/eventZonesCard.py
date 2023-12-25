#from events\subevents\eventZone.py import EventZone
#imports
class EventZonesCard(EventZone):
    def __init__(self, id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner, effect_card, effect_card_owner):
        super().__init__(id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner)
        self.effect_card_owner = effect_card_owner
        self.effect_card = effect_card
    def execute(self):
        for card in self.moving_card:
            self.new_zone.add_card(self.old_zone.remove_card(card))