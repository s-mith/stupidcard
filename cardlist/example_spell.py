import uuid
from cardSpell import CardSpell
from effectCard import EffectCard
from eventZonesPlayer import EventZonesPlayer
#imports
def example_maker(owner):
    example = CardSpell("cardname", 0, {}, "id", "description", str(uuid.uuid4()), owner)

    def pot_of_greed_effect(gamemaster, event, stage,player):
        if stage == ("adding_event", "added_event", "excuted_event"):
            if event.id == "play":
                if event.card == example:
                    # some event
                    pass

    example.effects["nameofeffect"] = EffectCard("pot of greed", None, lambda gamemaster, event, stage,player: pot_of_greed_effect(gamemaster, event, stage, player), pot_of_greed, owner)
    
    return example