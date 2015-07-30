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
        while self.__player.ActionPoints > 0:
            try:
                doAttack = random.randint(1,1000)
                if self.CanAttack(opponent) and doAttack % 3 == 0:
                    highest = self.__player.VisibleCards[0]
                    lowest = opponent.VisibleCards[0]
                    
                    for c in self.__player.VisibleCards:
                        if c.AP > highest.AP:
                            highest = c
                    
                    for c in opponent.VisibleCards:
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
                    highest = self.__player.hand[0]
                    
                    for c in self.__player.VisibleCards:
                        if c.DP > highest.DP:
                            highest = c
                    
                    self.__player.PutCard(highest)
                    self.__controller.AddAction(Actions.PLACE_CARD, card=highest)
                    self.__actions += 1
                else:
                    break
            except:
                break
        try:
            r = random.randint(0,1000)
            if r % 2 == 0:
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
                if len(opponent.VisibleCards) > 0:
                    return True
        return False
    
    def CanPlaceCard(self):
        if self.__player.ActionPoints > self.__player.CARD_COST:
            return True
        return False
    
    def MustDrawCard(self):
        if len(self.__player.hand) < 1:
            return True
        else:
            return False