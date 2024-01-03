from eventState import EventState
from gameMaster import GameMaster
from state import State
from player import Player


class EventStateIncrementPlayer(EventState):
    def __init__(self, id, gamemaster, owner: GameMaster, state: State,player_current:Player):
        super().__init__(id, gamemaster, owner, state)
        self.player_current = player_current
        
    def execute(self):
        self.state.swap_player()

