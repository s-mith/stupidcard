class EffectCard(Effect):
    def __init__(self, id, event,  func, funcif,card, card_owner):
        super().__init__(id, event, func,funcif)
        self.card = card
        self.card_owner = card_owner