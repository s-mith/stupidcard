from player import Player
from zoneEventStack import ZoneEventStack
from zoneTrash import ZoneTrash

class State:
    def __init__(self, player1: Player, player2: Player, stack: ZoneEventStack, trash: ZoneTrash):
        self.player1 = player1
        self.player2 = player2
        self.stack = stack
        self.trash = trash
        self.turn = 0
        self.player = None
        self.priority = None

    def increment_turn(self):
        self.turn += 1

    def decrement_turn(self):
        self.turn -= 1

    def set_turn(self, turn):
        self.turn = turn

    def swap_player(self):
        if self.player == self.player1:
            self.player = self.player2
        else:
            self.player = self.player1
    
    def swap_priority(self):
        if self.priority == self.player1:
            self.priority = self.player2
        else:
            self.priority = self.player1

    def set_player(self, player):
        self.player = player

    def set_priority(self, player):
        self.priority = player

    def add_event(self, event):
        self.stack.add_event(event)

    def get_top_event(self):
        return self.stack.get_top()
    
    def run_all_effects(self, event):
        self.player1.check_all_effects(event)
        self.player2.check_all_effects(event)
        