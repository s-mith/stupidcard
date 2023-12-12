from zoneCard import ZoneCard
from card import Card
import random

class ZoneCardDeck(ZoneCard):
    def __init__(self, id, cards:list[Card]):
        super().__init__(id)
        self.cards = cards
    
    def shuffle(self):
        # randomize the order of the cards in the deck
        tempdeck = []
        while len(self.cards) > 0:
            randindex = random.randint(0, len(self.cards) - 1)
            tempdeck.append(self.cards[randindex])
            self.cards.pop(randindex)
        self.cards = tempdeck

    def get_top(self):
        # return the top card of the deck
        return self.cards[0]
    

    def get_top_creature(self):
        # return the top card of the deck
        for card in self.cards:
            if card.is_creature():
                return card
        return None
    
    def get_top_spell(self):
        # return the top card of the deck
        for card in self.cards:
            if card.is_spell():
                return card
        return None

    
