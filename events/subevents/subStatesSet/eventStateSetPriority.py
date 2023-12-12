from eventState import EventState
from gameMaster import GameMaster
from state import State
from player import Player
from typing import Union

class EventStateSetPriority(EventState):
    def __init__(self, id, gamemaster: GameMaster, state: State, priority_current: Union[Player, None], priority_next: Union[Player, None]):
        super().__init__(id, gamemaster, state)
        self.priority_current = priority_current
        self.priority_next = priority_next
        
    def execute(self):
        self.state.set_priority(self.priority_next)

