from zoneCardDeck import ZoneCardDeck
from zoneCardHand import ZoneCardHand
from zoneCardBattlefield import ZoneCardBattlefield
from zoneCardGraveyard import ZoneCardGraveyard
from zoneEffectOrderable import ZoneEffectOrderable
from effectPlayer import EffectPlayer
from eventZonesPlayer import EventZonesPlayer
from eventZonePlayer import EventZonePlayer
#imports
class Player:
    def __init__(self, id, deck_, handsize, life, mana, max_mana, effects) -> None:
        self.id = id
        self.deck = ZoneCardDeck(id+"_deck", deck_)
        self.hand = ZoneCardHand(id+"_hand", handsize)
        self.battlefield = ZoneCardBattlefield(id+"_battlefield")
        self.graveyard = ZoneCardGraveyard(id+"_graveyard")
        self.effectZone = ZoneEffectOrderable(id+"_effectZone", [])
        self.effects = effects
        self.effects["draw"] = EffectPlayer("draw_"+self.id, None, lambda gamemaster, event, args: EventZonesPlayer("EventZonePlayer", gamemaster, self.deck.get_n_top(event), self.deck, self.hand, self, self, self), None, self)
        self.effects["play"] = EffectPlayer("play_"+self.id, None,lambda gamemaster,event, player: EventZonePlayer("play", gamemaster, self.hand.cards[event], self.hand, self.graveyard, self, self, self) if type(self.hand.cards[event]) == CardSpell else EventZonePlayer("EventZonePlayer", gamemaster, self.hand.cards[event], self.hand, self.battlefield, self, self, self),None, self)
        self.life = life
        self.mana = mana
        self.turn_mana = 0
        self.max_mana = max_mana
    def set_life(self, life):
        self.life = life
        return self.life
    def set_mana(self, mana):
        self.mana = mana
        return self.mana
    def all_cards(self):
        return self.deck.cards + self.hand.cards + self.battlefield.cards + self.graveyard.cards
    def all_cards_in_zone(self, zone):
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
    def execute_effects(self, gamemaster, event, stage, player):
        for effect in self.effects:
            effect.execute(gamemaster, event, stage, player)
