import uuid
from cardSpell import CardSpell
from effectCard import EffectCard
from eventZonesPlayer import EventZonesPlayer
#imports
def pot_of_greed_maker(owner):
    pot_of_greed = CardSpell("pot of greed", 0, {}, "3", "draw 2 cards", str(uuid.uuid4()), owner)

    def pot_of_greed_effect(gamemaster, event, stage,player):
        if stage == "added_event":
            if event.id == "play":
                if event.card == pot_of_greed:
                    EventZonesPlayer("pot_of_greed_event", gamemaster, player.deck.get_top_x(2), player.deck, player.hand, player, player, owner)

    
    pot_of_greed.effects["onPlay"] = EffectCard("pot of greed", None, lambda gamemaster, event, stage,player: pot_of_greed_effect(gamemaster, event, stage, player), pot_of_greed, owner)
    
    return pot_of_greed