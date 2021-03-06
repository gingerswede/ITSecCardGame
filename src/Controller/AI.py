'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
@copyright: 2015 Emil Carlsson
@license: This program is distributed under the terms of the GNU General Public License
'''
import random
from Model.Actions import Actions
from Model.Exceptions import OutOfMovesError

class AI(object):
    
    __player = None
    __controller = None
    __actions = None
    
    def __init__(self, player, gameController, *args, **kwargs):
        self.__player = player
        self.__controller = gameController
        self.__actions = 0
        
    def MakeMove(self, opponent):
        self.__actions = 0
        counter = 0
        try:
            if self.__player.CardsLeft < 2 and self.__player.CanDrawCard: #force the AI to empty their deck.
                self.__player.DrawCard()
                self.__controller.AddAction(Actions.DRAW_CARD)
                self.__actions += 1
        except:
            pass
        while self.__player.ActionPoints > self.__player.ATTACK_COST:
            if counter > 3:
                break
            #to prevent an endless loop, the loop will only continue while at least one attack can be made
            try:
                doAttack = random.randint(1,1000)
                if self.CanAttack(opponent) and doAttack % 6 < 5: #random factor to not make it unbeatable
                    highest = self.__player.VisibleCards[0]
                    lowest = opponent[0]
                    
                    for c in self.__player.VisibleCards:
                        if c.AP > highest.AP:
                            highest = c
                    
                    for c in opponent:
                        if c.DP < highest.AP:
                            lowest = c
                    
                    if highest.AP > lowest.DP:
                        winner = self.__player.Attack(lowest, highest)
                        self.__controller.AddAction(Actions.ATTACK, attacker=highest, defender=lowest, winner=winner)
                        self.__actions += 1
                    
                if self.MustDrawCard() or (self.__player.CanDrawCard and doAttack % 7 == 0):
                    self.__player.DrawCard()
                    self.__controller.AddAction(Actions.DRAW_CARD)
                    self.__actions += 1
                    
                if self.CanPlaceCard():
                    highest = self.__player.hand[random.randint(0, len(self.player.hand)-1)]
                    
                    for c in self.__player.VisibleCards:
                        if c.DP > highest.DP:
                            highest = c
                    
                    self.__player.PutCard(highest)
                    self.__controller.AddAction(Actions.PLACE_CARD, card=highest)
                    self.__actions += 1
            except:
                break
        try:
            r = random.randint(0,1000)
            if r % 7 == 0: #random factor to not make it unbeatable
                self.__player.DrawCard()
            else:
                card = self.__player.hand[r % len(self.__player.hand)]
                self.__player.PutCard(card)
                self.__controller.AddAction(Actions.PLACE_CARD, card=card)
                self.__actions += 1
        except:
            pass
        
        self.__player.EndTurn()
        
        if self.__actions == 0:
            self.__controller.AddAction(Actions.PASS)
        
        return True
    
    def CanAttack(self, opponent):
        if self.__player.ActionPoints > self.__player.CARD_COST:
            if len(self.__player.VisibleCards) > 0:
                if len(opponent) > 0:
                    return True
        return False
    
    def CanPlaceCard(self):
        if self.__player.ActionPoints > self.__player.CARD_COST:
            return True
        return False
    
    def MustDrawCard(self):
        if len(self.__player.hand) < 1 or (len(self.__player.VisibleCards) == self.__player.MAX_VISIBLE_CARDS and len(self.__player.hand) < self.__player.MAX_HAND_SIZE):
            return True
        else:
            return False