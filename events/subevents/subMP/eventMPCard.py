class EventMPCard(EventMP):
    def __init__(self, id, gamemaster, owner, old_mp, new_mp, target_player, effect_card_owner, effect_card):
        super().__init__(id, gamemaster, owner, old_mp, new_mp, target_player)
        self.effect_card_owner = effect_card_owner
        self.effect_card = effect_card