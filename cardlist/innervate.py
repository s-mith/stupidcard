from cardSpell import CardSpell
from effectCard import EffectCard
from eventMPCard import EventMPCard
#imports
innervate = CardSpell("innervate", 0, {}, "2", "add 2 mana", str(uuid.uuid4()))


def innervate_effect(gamemaster, event, player):
    EventMPCard("innervate_event", gamemaster, player.mana, player.mana + 2, player, player, None)


innervate.effects["onPlay"] = EffectCard("innervate", None, lambda gamemaster, event, player: innervate_effect(gamemaster,event,player), None ,None, None)
