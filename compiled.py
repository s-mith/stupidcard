import uuid
import random
class Event:
    def __init__(self, id, gamemaster):
        self.id = id 
        self.gamemaster = gamemaster
        self.gamemaster.add_event(self)
    def execute(self):
        pass
class EventZone(Event):
    def __init__(self, id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner):
        super().__init__(id, gamemaster)
        self.moving_card = moving_card
        self.old_zone = old_zone
        self.new_zone = new_zone
        self.old_zone_owner = old_zone_owner
        self.new_zone_owner = new_zone_owner
    def execute(self):
        self.new_zone.add_card(self.old_zone.remove_card(self.moving_card))

class EventZonePlayer(EventZone):
    def __init__(self, id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner, effect_player):
        super().__init__(id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner)
        self.owner = effect_player

class EventZonesCard(EventZone):
    def __init__(self, id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner, effect_card, effect_card_owner):
        super().__init__(id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner)
        self.effect_card_owner = effect_card_owner
        self.effect_card = effect_card
    def execute(self):
        for card in self.moving_card:
            self.new_zone.add_card(self.old_zone.remove_card(card))

class EventZonesCard(EventZone):
    def __init__(self, id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner, effect_card, effect_card_owner):
        super().__init__(id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner)
        self.effect_card_owner = effect_card_owner
        self.effect_card = effect_card
    def execute(self):
        for card in self.moving_card:
            self.new_zone.add_card(self.old_zone.remove_card(card))

class EventZonesPlayer(EventZone):
    def __init__(self, id, gamemaster, moving_card, old_zone, new_zone, old_zone_owner, new_zone_owner, effect_player):
        super().__init__(id, gamemaster, None, old_zone, new_zone, old_zone_owner, new_zone_owner)
        self.owner = effect_player
        self.moving_card = moving_card
    def execute(self):
        if type(self.moving_card) == list:
            for card in self.moving_card:
                self.new_zone.add_card(self.old_zone.remove_card(card))
        else:
            self.new_zone.add_card(self.old_zone.remove_card(self.moving_card)) 
class EventZonesDoubleCard():
    def __init__(self, id, gamemaster, moving_cards1, moving_cards2, old_zone1, new_zone1, old_zone2, new_zone2, old_zone_owner1, new_zone_owner1, old_zone_owner2, new_zone_owner2):
        self.id = id
        self.gamemaster = gamemaster
        self.moving_cards1 = moving_cards1
        self.moving_cards2 = moving_cards2
        self.old_zone1 = old_zone1
        self.new_zone1 = new_zone1
        self.old_zone2 = old_zone2
        self.new_zone2 = new_zone2
        self.old_zone_owner1 = old_zone_owner1
        self.new_zone_owner1 = new_zone_owner1
        self.old_zone_owner2 = old_zone_owner2
        self.new_zone_owner2 = new_zone_owner2
        self.gamemaster.add_event(self)
    def execute(self):
        for card in self.moving_cards1:
            self.new_zone1.add_card(self.old_zone1.remove_card(card))
        for card in self.moving_cards2:
            self.new_zone2.add_card(self.old_zone2.remove_card(card))
# from events\event.py import Event
# from events\subevents\subZone\EventZonesDoubleCard import EventZonesDoubleCard
# imports
class EventGameStart(Event):
    def __init__(self, id, gamemaster, players):
        super().__init__(id, gamemaster)
        self.players = players
    def execute(self):
        self.gamemaster.state.set_player(self.players[1])
        EventZonesDoubleCard("EventZonesDoubleCard", self.gamemaster, [self.players[0].deck.get_n_top(i) for i in range(5)], [self.players[1].deck.get_n_top(i) for i in range(5)], self.players[0].deck, self.players[0].hand, self.players[1].deck, self.players[1].hand, self.players[0], self.players[0], self.players[1], self.players[1])

class EventMP(Event):
    def __init__(self, id, gamemaster, old_mp, new_mp, target_player):
        super().__init__(id, gamemaster)
        self.old_mp = old_mp
        self.new_mp = new_mp
        self.target_player = target_player
    
    def execute(self):
        self.target_player.set_mana(self.new_mp)
class EventMPCard(EventMP):
    def __init__(self, id, gamemaster, old_mp, new_mp, target_player, effect_card_owner, effect_card):
        super().__init__(id, gamemaster, old_mp, new_mp, target_player)
        self.effect_card_owner = effect_card_owner
        self.effect_card = effect_card
class Effect:
    def __init__(self,id, event, func, funcif):
        self.id = id
        self.event = event
        self.func = func
        self.funcif = funcif
    def ifexecute(self, gamemaster,event, player):
        if self.funcif(gamemaster, self.event, player):
            return self.execute(gamemaster, player)
        else:
            return None
    def execute(self, gamemaster,event, player):  
        # spread out the args
        self.func(gamemaster, event, player)
class EffectCard(Effect):
    def __init__(self, id, event,  func, funcif,card, card_owner):
        super().__init__(id, event, func,funcif)
        self.card = card
        self.card_owner = card_owner
class EffectPlayer(Effect):
    def __init__(self,id ,  event, func, funcif, player):
        super().__init__(id, event, func,funcif)
        self.player = player
class Card:
    def __init__(self, name, cost, effects, text, id, gameid):
        self.name = name
        self.cost = cost
        self.effects = effects
        self.text = text
        self.id = id
        self.gameid = gameid
    def execute_effects(self, gamemaster):
        # execute_effects 
        _effects = []
        for effect in self.effects:
            x = effect.execute(gamemaster)
            _effects.append(x) if x != None else None
        return _effects
    def is_creature(self):
        return False
    def is_spell(self):
        return False
class CardCreature(Card):
    def __init__(self, name, cost, effects, text, id, gameid, attack, life):
        super().__init__(name, cost, effects, text, id, gameid)
        self.attack = attack
        self.life = life
    def set_life(self, life):
        self.life = life
    def is_creature(self):
        return True
    def is_spell(self):
        return False
class CardSpell(Card):
    def __init__(self, name, cost, effects, text, id, gameid):
        super().__init__(name, cost, effects, text, id, gameid)
    def is_creature(self):
        return False
    def is_spell(self):
        return True
class Zone:
    def __init__(self, id):
        self.name = id
class ZoneCard(Zone):
    def __init__(self, id):
        super().__init__(id)
        self.cards= []
    def size(self):
        return len(self.cards)
    def add_card(self, card):
        self.cards.append(card)
        return card
    def remove_card(self, card):
        self.cards.remove(card)
        return card
    def count(self):
        return len(self.cards)
    

class ZoneCardHand(ZoneCard):
    def __init__(self, id,max_size):
        super().__init__(id)
        self.max_size = max_size
    def get_random_n(self, n):
        if n > self.size():
            return random.sample(self.cards, self.size())
        return random.sample(self.cards, n)
class ZoneCardDeck(ZoneCard):
    def __init__(self, id, cards):
        super().__init__(id)
        self.cards = cards
    def shuffle(self):
        tempdeck = []
        while len(self.cards) > 0:
            randindex = random.randint(0, len(self.cards) - 1)
            tempdeck.append(self.cards[randindex])
            self.cards.pop(randindex)
        self.cards = tempdeck
    def get_top(self):
        return self.cards[0]
    def get_n_top(self, n):
        return self.cards[n]
    def get_top_x(self, x):
        if x > self.size():
            return self.cards
        return self.cards[:x]
    def get_top_creature(self):
        for card in self.cards:
            if card.is_creature():
                return card
        return None
    def get_top_spell(self):
        for card in self.cards:
            if card.is_spell():
                return card
        return None
class ZoneCardGraveyard(ZoneCard):
    def __init__(self, id):
        super().__init__(id)
    def get_top(self):
        return self.cards[0]
    def get_top_creature(self):
        for card in self.cards:
            if card.is_creature():
                return card
        return None
    def get_top_spell(self):
        for card in self.cards:
            if card.is_spell():
                return card
        return None
class ZoneCardBattlefield(ZoneCard):
    def __init__(self, id):
        super().__init__(id)
class ZoneEffect(Zone):
    def __init__(self, id, effects):
        super().__init__(id)
        self.effects = effects
    def add_effect(self, effect):

        self.effects.append(effect)
        return effect

    def remove_effect(self, effect):

        self.effects.remove(effect)
        return effect

    def count(self):
        return len(self.effects) 
class ZoneEffectOrderable(ZoneEffect):
    def __init__(self, id, effects):
        super().__init__(id, effects)
    def add_effect(self, effect):
        
        self.effects.append(effect)
        return effect

    def remove_effect(self, effect):

        self.effects.remove(effect)
        return effect

    def reorder_effects(self, order):
        self.effects = [self.effects[i] for i in order]
class ZoneEvent(Zone):
    def __init__(self, id, events):
        super().__init__(id)
        self.events = events
    def add_event(self, event):
        self.events.append(event)
    def remove_event(self, event):
        if isinstance(event):
            self.events.remove(event)
            return event
        else:
            print("Error: event is not a event")
    def count(self):
        return len(self.events) 
class ZoneEventStack(ZoneEvent):
    def __init__(self, id, events):
        super().__init__(id, events)
        self.events = events
    def add_event(self, event):
        self.events.append(event)
        return event
    def remove_event(self, event):
        self.events.remove(event)
        return event
    def look_top(self):
        return self.events[0]
    def get_top(self):
        return self.events.pop()
class ZoneTrash(Zone):
    def __init__(self, id):
        super().__init__(id)
    def add(self, thing):
        pass
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
        self.effects["play"] = EffectPlayer("play_"+self.id, None,lambda gamemaster,event, player: EventZonePlayer("EventZonePlayer", gamemaster, self.hand.cards[event], self.hand, self.graveyard, self, self, self) if type(self.hand.cards[event]) == CardSpell else EventZonePlayer("EventZonePlayer", gamemaster, self.hand.cards[event], self.hand, self.battlefield, self, self, self),None, self)
        self.life = life
        self.mana = mana
        self.turn_mana = 0
        self.max_mana = max_mana
    def draw(self, gamemaster, n=1):
        self.effects["draw"].execute(gamemaster, n, self)
    def play(self, gamemaster, cardnumber):
        # check if the card has a play effect
        if "onPlay" in self.hand.cards[cardnumber].effects:
            self.hand.cards[cardnumber].effects["onPlay"].execute(gamemaster, None,self)
        self.effects["play"].execute(gamemaster, cardnumber, self)
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
    def check_all_effects(self, event):
        for card in self.all_cards():
            x = card.execute_effects(event)
            [self.effectZone.add_effect(i) for i in x] if x != [] else None
        for effect in self.effects:
            x = effect.execute(event)
            [self.effectZone.add_effect(i) for i in x] if x != [] else None
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





blackjack = CardSpell("blackjack", 0, {}, "the player who has less than and is closer to 21 cards in their deck draws 2 cards and the other player discards a card", "4", str(uuid.uuid4()))


def blackjack_effect(gamemaster, event, player):
    player1 = gamemaster.state.player1
    player2 = gamemaster.state.player2

    total_mana_cost1 = sum(card.mana_cost for card in player1.hand)
    total_mana_cost2 = sum(card.mana_cost for card in player2.hand)

    if total_mana_cost1 <= 21 and (total_mana_cost2 > 21 or total_mana_cost1 > total_mana_cost2):
        EventZonesDoubleCard("Blackjack_winner="+player1.id, gamemaster, player1.deck.get_n_top(2), player2.hand.get_random(2), player1.deck, player1.hand, player2.hand, player2.graveyard, player1, player1, player2, player2)
    elif total_mana_cost2 <= 21 and (total_mana_cost1 > 21 or total_mana_cost2 > total_mana_cost1):
        EventZonesDoubleCard("Blackjack_winner="+player2.id, gamemaster, player2.deck.get_n_top(2), player1.hand.get_random(2), player2.deck, player2.hand, player1.hand, player1.graveyard, player2, player2, player1, player1)
        
    


blackjack.effects["onPlay"] = EffectCard("blackjack", None, lambda gamemaster, event, player: blackjack_effect(gamemaster, event, player),None, None,None)


brainwormed_transgirl = CardCreature("brainwormed transgirl", 2, {}, "5", "when brainwormed transgirl enters the battlefield, you discard a card import your hand \n whenever brainwormed transgirl attacks your opponent discards a card", str(uuid.uuid4()), 3, 2)


innervate = CardSpell("innervate", 0, {}, "2", "add 2 mana", str(uuid.uuid4()))


def innervate_effect(gamemaster, event, player):
    EventMPCard("innervate_event", gamemaster, player.mana, player.mana + 2, player, player, None)


innervate.effects["onPlay"] = EffectCard("innervate", None, lambda gamemaster, event, player: innervate_effect(gamemaster,event,player), None ,None, None)


pot_of_greed = CardSpell("pot of greed", 0, {}, "3", "draw 2 cards", str(uuid.uuid4()))

def pot_of_greed_effect(gamemaster, event,player):
    EventZonesPlayer("pot_of_greed_event", gamemaster, player.deck.get_top_x(2), player.deck, player.hand, player, player, player)

pot_of_greed.effects["onPlay"] = EffectCard("pot of greed", None, lambda gamemaster, event, args: pot_of_greed_effect(gamemaster,event,args), None , None, None)




chillwind_yeti = CardCreature("chillwind yeti", 4, {}, "1", "", str(uuid.uuid4()), 4, 5)



cards = {
    1: chillwind_yeti,
    2: innervate,
    3: pot_of_greed,
    4: blackjack,
    5: brainwormed_transgirl
    }



lusiodeck = [cards[random.randint(1,4)] for i in range(60)]
weinordeck = [cards[random.randint(1,4)] for i in range(60)]


P1 = Player("lusio", lusiodeck, 10, 20, 0,10,{})
P2 = Player("weinor", weinordeck, 10, 20, 0,10,{})
GM = GameMaster(P1,P2)
GM.mainLoop() 