from eventState import EventState
from gameMaster import GameMaster
from state import State
from player import Player


class EventStateIncrementPriority(EventState):
    def __init__(self, id, gamemaster: GameMaster, state: State,priority_current:Player):
        super().__init__(id, gamemaster, state)
        self.priority_current = priority_current
        
    def execute(self):
        self.state.swap_priority()

