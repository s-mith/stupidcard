from eventState import EventState
from gameMaster import GameMaster
from state import State

class EventStateSetTurn(EventState):
    def __init__(self, id, gamemaster: GameMaster, state: State,turn_current:int, turn_next:int):
        super().__init__(id, gamemaster, state)
        self.turn_current = turn_current
        self.turn_next = turn_next
        
    def execute(self):
        self.state.set_turn(self.turn_next)

