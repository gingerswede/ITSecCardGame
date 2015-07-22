'''
Created on 21 jul 2015

@author: Emil
'''
from Model.Deck import Deck

from argparse import ArgumentError

from Model.Exceptions import OutOfMovesError

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
    
    def __init__(self, *args, **kwargs):
        if self.DECK in kwargs:
            self.NewGame(kwargs[self.DECK])
        else:
            raise ArgumentError
    
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
    
    def DrawCard(self):
        if self.CanDrawCard and len(self.VisibleCards) <= self.MAX_VISIBLE_CARDS:
            self.__visibleCards.append(self.__deck.DrawCard())            
        else:
            raise OutOfMovesError
    
    def PutCard(self):
        if not self.__deck.OutOfCards and self.ActionPoints >= self.CARD_COST:
            self.__actionPoints -= self.CARD_COST
            self.__visibleCards.append(self.__deck.DrawCard())
    
    def EndTurn(self):
        self.__actionPoints = self.MAX_ACTION_POINTS
        
    def NewGame(self, deck):
        self.__deck = deck
        self.__actionPoints = self.MAX_ACTION_POINTS
        self.__canDrawCard = True
        self.__visibleCards = []
        self.__hand = []