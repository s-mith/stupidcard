from event import Event
from player import Player
from gameMaster import GameMaster
from state import State


class EventState(Event):
    def __init__(self, id, gamemaster: GameMaster, state: State):
        super().__init__(id, gamemaster)
        self.state = state
    