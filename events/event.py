class Event:
    def __init__(self, id, gamemaster):
        self.id = id 
        self.gamemaster = gamemaster
        self.gamemaster.add_event(self)
    def execute(self):
        pass