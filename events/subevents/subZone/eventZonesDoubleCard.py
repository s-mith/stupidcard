class EventZonesDoubleCard():
    def __init__(self, id, gamemaster, moving_cards1, moving_cards2, old_zone1, new_zone1, old_zone2, new_zone2, old_zone_owner1, new_zone_owner1, old_zone_owner2, new_zone_owner2):
        self.id = id
        self.gamemaster = gamemaster
        self.moving_cards1 = moving_cards1
        self.moving_cards2 = moving_cards2
        self.old_zone1 = old_zone1
        self.new_zone1 = new_zone1
        self.old_zone2 = old_zone2
        self.new_zone2 = new_zone2
        self.old_zone_owner1 = old_zone_owner1
        self.new_zone_owner1 = new_zone_owner1
        self.old_zone_owner2 = old_zone_owner2
        self.new_zone_owner2 = new_zone_owner2
        self.gamemaster.add_event(self)
    def execute(self):
        for card in self.moving_cards1:
            self.new_zone1.add_card(self.old_zone1.remove_card(card))
        for card in self.moving_cards2:
            self.new_zone2.add_card(self.old_zone2.remove_card(card))