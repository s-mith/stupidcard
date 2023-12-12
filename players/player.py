from zoneCardBattlefield import ZoneCardBattlefield
from zoneCardGraveyard import ZoneCardGraveyard
from zoneCardHand import ZoneCardHand
from zoneCardDeck import ZoneCardDeck
from card import Card
from effectPlayer import EffectPlayer
from zoneEffectOrderable import ZoneEffectOrderable
from zonePermanence import ZonePermanence
from effect import Effect
from eventZonePlayer import EventZonePlayer
from event import Event




class Player:
    def __init__(self, id, deck_:list[Card], handsize:int, life:int, mana:int, max_mana:int, effects:list[Effect]) -> None:
        self.id = id
        self.deck = ZoneCardDeck(id+"_deck", deck_)
        self.hand = ZoneCardHand(id+"_hand", handsize)
        self.battlefield = ZoneCardBattlefield(id+"_battlefield")
        self.graveyard = ZoneCardGraveyard(id+"_graveyard")
        self.effectZone = ZoneEffectOrderable(id+"_effectZone", [])
        self.effects = effects
        self.permanence = ZonePermanence(id+"_permanence", [])
        self.life = life
        self.mana = mana
        self.max_mana = max_mana

    def set_life(self, life:int) -> int:
        self.life = life
        return self.life
    
    def set_mana(self, mana:int) -> int:
        self.mana = mana
        return self.mana

    def all_cards(self) -> list[Card]:
        return self.deck.cards + self.hand.cards + self.battlefield.cards + self.graveyard.cards
    
    def all_cards_in_zone(self, zone) -> list[Card]:
        if zone == "deck":
            return self.deck.cards
        elif zone == "hand":
            return self.hand.cards
        elif zone == "battlefield":
            return self.battlefield.cards
        elif zone == "graveyard":
            return self.graveyard.cards
        else:
            print("Error: zone not found")
            return []
        
    def check_all_effects(self, event: Event):
        # check_all_effects will return a list of effects that are triggered by the event
        # it will also add the effects to the effectZone
        # check cards player and permanence
        for card in self.all_cards():
            x = card.execute_effects(event)
            [self.effectZone.add_effect(i) for i in x] if x != [] else None
        for effect in self.effects:
            x = effect.execute(event)
            [self.effectZone.add_effect(i) for i in x] if x != [] else None
        # for permanence in 
        #     x = permanence.execute_effects(event)

    

