from eventState import EventState
from gameMaster import GameMaster
from state import State

class EventStateIncrementTurn(EventState):
    def __init__(self, id, gamemaster, owner: GameMaster, state: State,turn_current:int):
        super().__init__(id, gamemaster, owner, state)
        self.turn_current = turn_current
        
    def execute(self):
        self.state.increment_turn()

