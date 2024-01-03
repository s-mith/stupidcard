class Effect:
    def __init__(self,id, event, stage, func):
        self.id = id
        self.event = event
        self.func = func
        self.stage = stage
    def execute(self, gamemaster,event, stage, player):  
        # spread out the args
        self.func(gamemaster, event, stage, player)