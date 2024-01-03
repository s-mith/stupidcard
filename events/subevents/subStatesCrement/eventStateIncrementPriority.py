from eventState import EventState
from gameMaster import GameMaster
from state import State
from player import Player


class EventStateIncrementPriority(EventState):
    def __init__(self, id, gamemaster, owner: GameMaster, state: State,priority_current:Player):
        super().__init__(id, gamemaster, owner, state)
        self.priority_current = priority_current
        
    def execute(self):
        self.state.swap_priority()

