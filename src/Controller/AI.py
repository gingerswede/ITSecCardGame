'''
Created on 28 jul 2015

@author: Emil
'''
from Model.Exceptions import OutOfMovesError
import random

class AI(object):
    
    __player = None
    
    def __init__(self, player, *args, **kwargs):
        self.__player = player
        
    def MakeMove(self, opponent):
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
                        self.__player.Attack(lowest, highest)
                    
                if self.MustDrawCard() or (self.__player.CanDrawCard and doAttack % 7 == 0):
                    self.__player.DrawCard()
                    
                if self.CanPlaceCard():
                    highest = self.__player.hand[0]
                    
                    for c in self.__player.VisibleCards:
                        if c.DP > highest.DP:
                            highest = c
                    
                    self.__player.PutCard(highest)
                else:
                    break
            except Exception as e:
                print e
                break
        try:
            self.__player.DrawCard()
        except:
            pass
        self.__player.EndTurn()
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