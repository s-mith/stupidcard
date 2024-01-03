# from events\event.py import Event
# from events\subevents\subZone\EventZonesDoubleCard import EventZonesDoubleCard
# imports
class EventGameStart(Event):
    def __init__(self, id, gamemaster, owner, players):
        super().__init__(id, gamemaster, owner)
        self.players = players
    def execute(self):
        self.gamemaster.state.set_player(self.players[1])
        EventZonesDoubleCard("EventZonesDoubleCard", self.gamemaster, [self.players[0].deck.get_n_top(i) for i in range(5)], [self.players[1].deck.get_n_top(i) for i in range(5)], self.players[0].deck, self.players[0].hand, self.players[1].deck, self.players[1].hand, self.players[0], self.players[0], self.players[1], self.players[1])
