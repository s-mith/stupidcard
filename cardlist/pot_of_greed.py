from cardSpell import CardSpell
from effectCard import EffectCard
from eventZonesPlayer import EventZonesPlayer
#imports
pot_of_greed = CardSpell("pot of greed", 0, {}, "3", "draw 2 cards", str(uuid.uuid4()))

def pot_of_greed_effect(gamemaster, event,player):
    EventZonesPlayer("pot_of_greed_event", gamemaster, player.deck.get_top_x(2), player.deck, player.hand, player, player, player)

pot_of_greed.effects["onPlay"] = EffectCard("pot of greed", None, lambda gamemaster, event, args: pot_of_greed_effect(gamemaster,event,args), None , None, None)


