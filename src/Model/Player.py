'''
Created on 21 jul 2015

@author: Emil
'''
from Model.Deck import Deck

from Model.Exceptions import OutOfMovesError, IncorrectAttackerError

class Player(object):
    DECK = 'deck'
    CARD_COST = 2
    ATTACK_COST = 1
    MAX_ACTION_POINTS = 3
    MAX_VISIBLE_CARDS = 4
    
    __actionPoints = None
    __deck = None
    __visibleCards = None
    __hand = None
    __canDrawCard = None
    __name = "Default player"
    
    def __init__(self, *args, **kwargs):
        if self.DECK in kwargs:
            self.NewGame(kwargs[self.DECK])
        
    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, name):
        self.__name = str(name)
    
    @property
    def ActionPoints(self):
        return self.__actionPoints
    
    @property
    def VisibleCards(self):
        return self.__visibleCards
    
    @property
    def CardsLeft(self):
        return self.__deck.NumberOfCardsLeft
    
    @property
    def CanDrawCard(self):
        if self.__canDrawCard and not self.__deck.OutOfCards:
            return True
        else:
            return False
    
    @property
    def hand(self):
        return self.__hand
        
    def DrawCard(self):
        if self.CanDrawCard and len(self.VisibleCards) <= self.MAX_VISIBLE_CARDS and self.__actionPoints >= self.CARD_COST:
            self.__hand.append(self.__deck.DrawCard())
            self.__actionPoints -= self.CARD_COST
        else:
            raise OutOfMovesError
    
    def PutCard(self, card):
        if self.ActionPoints >= self.CARD_COST and card in self.__hand:
            self.__actionPoints -= self.CARD_COST
            self.__hand.remove(card)
            self.__visibleCards.append(card)
    
    def EndTurn(self):
        self.__actionPoints = self.MAX_ACTION_POINTS
        
    def Attack(self, defender, attacker):
        if attacker in self.__visibleCards:
            if self.ActionPoints > 0:
                self.__actionPoints -= self.ATTACK_COST
                return defender.defend(attacker)
            else:
                raise OutOfMovesError
        else:
            raise IncorrectAttackerError
        
    def ClearBoard(self):
        for c in self.__visibleCards:
            if not c.IsAlive:
                self.__visibleCards.remove(c)
        
    def NewGame(self, deck):
        self.__deck = deck
        self.__actionPoints = self.MAX_ACTION_POINTS
        self.__canDrawCard = True
        self.__visibleCards = []
        self.__hand = []