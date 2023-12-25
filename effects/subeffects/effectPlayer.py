class EffectPlayer(Effect):
    def __init__(self,id ,  event, func, funcif, player):
        super().__init__(id, event, func,funcif)
        self.player = player