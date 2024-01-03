from eventState import EventState
from gameMaster import GameMaster
from state import State
from player import Player
from typing import Union

class EventStateSetPlayer(EventState):
    def __init__(self, id, gamemaster, owner: GameMaster, state: State, player_current: Union[Player, None], player_next: Union[Player, None]):
        super().__init__(id, gamemaster, owner, state)
        self.player_current = player_current
        self.player_next = player_next
        
    def execute(self):
        self.state.set_player(self.player_next)

