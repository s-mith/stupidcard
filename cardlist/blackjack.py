from cardSpell import CardSpell
from effectCard import EffectCard
from eventZonesDoubleCard import EventZonesDoubleCard
#imports
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
