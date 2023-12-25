import uuid
import random
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\events\event.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\events\subevents\eventZone.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\events\subevents\subZone\eventZonePlayer.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\events\subevents\subZone\EventZonesCard.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\events\subevents\subZone\EventZonesCard.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\events\subevents\subZone\EventZonesPlayer.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\events\subevents\subZone\EventZonesDoubleCard.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\events\subevents\eventGameStart.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\events\subevents\eventMP.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\events\subevents\subMP\eventMPCard.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\effects\effect.py
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\effects\subeffects\effectCard.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\effects\subeffects\effectPlayer.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\cards\card.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\cards\subcards\cardCreature.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\cards\subcards\cardSpell.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\zones\zone.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\zones\subzones\zoneCard.py
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\zones\subzones\subcards\zoneCardHand.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\zones\subzones\subcards\zoneCardDeck.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\zones\subzones\subcards\zoneCardGraveyard.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\zones\subzones\subcards\zoneCardBattlefield.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\zones\subzones\zoneEffect.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\zones\subzones\subeffects\zoneEffectOrderable.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\zones\subzones\zoneEvent.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\zones\subzones\subevents\zoneEventStack.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\zones\subzones\zoneTrash.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\players\player.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\states\state.py 
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\gamemasters\gameMaster.py 


# cards!

#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\cardlist\blackjack.py
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\cardlist\brianwormed_transgirl.py
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\cardlist\innervate.py
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\cardlist\pot_of_greed.py
#import C:\Users\bobdsmith1\Desktop\projects\stupidcard\stupidcard\cardlist\chillwind_yeti.py

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