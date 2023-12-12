from player import Player
from card import Card
from eventZonePlayer import EventZonePlayer
from state import State
from effect import Effect

class GameMaster:
    def __init__(self, player1: Player, player2: Player):
        self.state = State(player1, player2)
        self.effects:dict[str, Effect] = {}
        


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
        
        
                    
            
            
    
        
    
    
        
        

