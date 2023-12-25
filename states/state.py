from zoneEventStack import ZoneEventStack
from zoneTrash import ZoneTrash
#imports
class State:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.stack = ZoneEventStack("stack", [])
        self.trash = ZoneTrash("trash")
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
    def look_top(self):
        return self.stack.look_top()
    def get_top(self):
        return self.stack.get_top()
    def eventlen(self):
        return self.stack.count()
    def run_all_effects(self, event):
        self.player1.check_all_effects(event)
        self.player2.check_all_effects(event)