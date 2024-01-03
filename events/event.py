class Event:
    def __init__(self, id, gamemaster, owner, owner):
        self.id = id 
        gamemaster.add_event(self, owner)
    def execute(self):
        pass