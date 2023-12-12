# events are things that happen in the game like a card moving from one zone to another, or a player or creature taking damage
from gameMaster import GameMaster
class Event:
    def __init__(self, id, gamemaster: GameMaster):
        self.id = id 
        self.gamemaster = gamemaster
        self.gamemaster.add_event(self)

    def execute(self):
        pass