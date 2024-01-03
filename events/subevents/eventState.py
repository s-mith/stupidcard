from event import Event
from player import Player
from gameMaster import GameMaster
from state import State


class EventState(Event):
    def __init__(self, id, gamemaster, owner: GameMaster, state: State):
        super().__init__(id, gamemaster, owner)
        self.state = state
    