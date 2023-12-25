class Effect:
    def __init__(self,id, event, func, funcif):
        self.id = id
        self.event = event
        self.func = func
        self.funcif = funcif
    def ifexecute(self, gamemaster,event, player):
        if self.funcif(gamemaster, self.event, player):
            return self.execute(gamemaster, player)
        else:
            return None
    def execute(self, gamemaster,event, player):  
        # spread out the args
        self.func(gamemaster, event, player)