from state import State
from eventGameStart import EventGameStart
#imports
class GameMaster:
    def __init__(self, player1, player2):
        self.state = State(player1, player2)
        self.effects = {}
    def all_cards(self):
        return self.state.player1.all_cards() + self.state.player2.all_cards()
    def all_cards_in_zone(self, zone):
        return self.state.player1.all_cards_in_zone(zone) + self.state.player2.all_cards_in_zone(zone)
    def get_card(self, id):
        for card in self.all_cards():
            if card.id == id:
                return card
        return None
    def add_event(self, event):
        self.state.add_event(event)
    def get_top_event(self):
        return self.state.get_top_event()
    def run_all_effects(self, event):
        self.state.run_all_effects(event)
    def event_priority_control(self, event):
        if hasattr(event, "owner"):
            if event.owner == self.state.player1:
                self.state.set_priority(self.state.player2)
            else:
                self.state.set_priority(self.state.player1)
        else:
            if self.state.player == self.state.player1:
                self.state.set_priority(self.state.player1)
            else:
                self.state.set_priority(self.state.player2)
    def priority_control(self):
            if self.state.player == self.state.player1:
                self.state.set_priority(self.state.player1)
            else:
                self.state.set_priority(self.state.player2)
    def interaction_window(self, player):
        print("\n"*30)
        print("mana: {}/{}".format(self.state.player1.mana, self.state.player1.turn_mana), "life: {}".format(self.state.player1.life), "deck: {}".format(self.state.player1.deck.count()), "graveyard: {}".format(self.state.player1.graveyard.count()), sep=" | ")
        print("{} hand: ".format(self.state.player1.id), ["{}:{}".format(i,card.name) for i,card in enumerate(self.state.player1.hand.cards)])
        print("{} battlefield: ".format(self.state.player1.id), ["{}:{}".format(i,card.name) for i,card in enumerate(self.state.player1.battlefield.cards)])
        print("\n{}\n".format(["{}:{}".format(i,event.id) for i,event in enumerate(self.state.stack.events)]) if self.state.eventlen() > 0 else "\n[]\n")
        print("{} battlefield: ".format(self.state.player2.id), ["{}:{}".format(i,card.name) for i,card in enumerate(self.state.player2.battlefield.cards)])
        print("{} hand: ".format(self.state.player2.id), ["{}:{}".format(i,card.name) for i,card in enumerate(self.state.player2.hand.cards)])
        print("mana: {}/{}".format(self.state.player2.mana, self.state.player2.turn_mana), "life: {}".format(self.state.player2.life), "deck: {}".format(self.state.player2.deck.count()), "graveyard: {}".format(self.state.player2.graveyard.count()), sep=" | ")
        return input("{}'s priority".format(player.id))
    def next_turn(self):
        if self.state.stack.count() > 0:
            return
        self.state.swap_player()
        if self.state.player1.turn_mana < self.state.player1.max_mana:
            self.state.player1.turn_mana += 1
        if self.state.player2.turn_mana < self.state.player2.max_mana:
            self.state.player2.turn_mana += 1
        self.state.player1.mana = self.state.player1.turn_mana
        self.state.player2.mana = self.state.player2.turn_mana
        self.state.player1.draw(self) if self.state.player == self.state.player2 else self.state.player2.draw(self)
        self.state.player.draw(self)
        self.state.increment_turn()
        print("TURN: {}".format(self.state.turn))
    def mainLoop(self):
        EventGameStart("EventGameStart", self, [self.state.player1, self.state.player2])
        loop = 0
        while True:
            print("loop: {}".format(loop))
            if self.state.eventlen() > 0:
                event = self.state.look_top()
                print(event.id)
                self.event_priority_control(event)
                action = self.interaction_window(self.state.priority) 
                action = int(action) if action.isdigit() else action
                print(action)
                if type(action) == int and self.state.player.hand.size() > action and self.state.player.mana >= self.state.player.hand.cards[action].cost:
                    self.state.priority.play(self, action)
                    self.state.player.mana -= self.state.player.hand.cards[action].cost
                checkevent = self.state.look_top()
                print(checkevent.id)
                action = ""
                if checkevent != event:
                    continue
                print("check")
                self.state.swap_priority()
                action = self.interaction_window(self.state.priority) 
                action = int(action) if action.isdigit() else action
                print(action)
                if type(action) == int and self.state.player.hand.size() > action and self.state.player.mana >= self.state.player.hand.cards[action].cost:
                    self.state.priority.play(self, action)
                    self.state.player.mana -= self.state.player.hand.cards[action].cost
                checkevent = self.state.look_top()
                action = ""
                if checkevent != event:
                    continue
                self.state.get_top().execute()
            elif self.state.eventlen() == 0:
                self.priority_control()
                action = self.interaction_window(self.state.priority) 
                action = int(action) if action.isdigit() else action
                print(action)
                if type(action) == int and self.state.player.hand.size() > action and self.state.player.mana >= self.state.player.hand.cards[action].cost:
                    self.state.priority.play(self, action)
                    self.state.player.mana -= self.state.player.hand.cards[action].cost
                action = ""
                self.state.swap_priority()
                action = self.interaction_window(self.state.priority) 
                action = int(action) if action.isdigit() else action
                print(action)
                if type(action) == int and self.state.player.hand.size() > action and self.state.player.mana >= self.state.player.hand.cards[action].cost:
                    self.state.priority.play(self, action)
                    self.state.player.mana -= self.state.player.hand.cards[action].cost
                action = ""
                self.next_turn()
            loop += 1
