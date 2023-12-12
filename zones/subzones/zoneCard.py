from card import Card
from zone import Zone
class ZoneCard(Zone):
    def __init__(self, id):
        super().__init__(id)
        self.cards:list[Card] = []

    def add_card(self, card: Card):
        # check to make sure card is a card
        if isinstance(card, Card):
            self.cards.append(card)
            return card
        else:
            print("Error: card is not a card")

    def remove_card(self, card: Card):
        # check to make sure card is a card
        if isinstance(card, Card):
            self.cards.remove(card)
            return card
        else:
            print("Error: card is not a card")

    def count(self):
        return len(self.cards)


    
    