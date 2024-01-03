class EffectPlayer(Effect):
    def __init__(self,id ,  event, func, player):
        super().__init__(id, event, func)
        self.player = player