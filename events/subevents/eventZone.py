class EventZone(Event):
    def __init__(self, id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner):
        super().__init__(id, gamemaster)
        self.moving_card = moving_card
        self.old_zone = old_zone
        self.new_zone = new_zone
        self.old_zone_owner = old_zone_owner
        self.new_zone_owner = new_zone_owner
    def execute(self):
        self.new_zone.add_card(self.old_zone.remove_card(self.moving_card))