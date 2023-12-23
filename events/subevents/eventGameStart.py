from event import Event
from eventZonePlayer import EventZonePlayer
from player import Player
from gameMaster import GameMaster







class EventGameStart(Event):
    def __init__(self, id, gamemaster:GameMaster, players:list[Player]):
        super().__init__(id, gamemaster)
        self.players = players
    
    def execute(self):
        for player in self.players:
            # draw 5 cards
            [EventZonePlayer(player.id + "_EventGameStart_draw", self.gamemaster, player.deck.get_top(), player.deck, player.hand, player, player) for i in range(5)]
    
    
