'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
@copyright: 2015 Emil Carlsson
@license: This program is distributed under the terms of the GNU General Public License
'''
from Model.Card import Card
import random

from _ctypes import ArgumentError

class Deck(object):
    
    MINIMUM_DECK_SIZE = 7
    MAXIMUM_DECK_SIZE = 14    
    DECK = 'deck'
    PLAYER_NAME = 'playerName'
    
    __deck = None
    __outOfCards = True

    def __init__(self, *args, **kwargs):
        self.__deck = []
        if kwargs is not None:
            if self.DECK in kwargs:
                if len(kwargs[self.DECK]) >= self.MINIMUM_DECK_SIZE and len(kwargs[self.DECK]) <= self.MAXIMUM_DECK_SIZE:
                    for c in kwargs[self.DECK]:
                        if isinstance(c, Card):
                            self.__deck.append(c)
                    
                    self.__outOfCards = False
                elif len(kwargs[self.DECK]) < self.MINIMUM_DECK_SIZE:
                    raise ArgumentError
                elif len(kwargs[self.DECK]) > self.MAXIMUM_DECK_SIZE:
                    raise ArgumentError
            
    def Shuffle(self):
        if self.__deck is None:
            raise TypeError
        
        else:
            shuffledDeck = [None] * len(self.__deck)
            numberOfCards = len(self.__deck)
            for i in range(0, numberOfCards):
                r = random.randint(0,len(self.__deck) - 1)                
                shuffledDeck[i] = self.__deck.pop(r)
                
            self.__deck = shuffledDeck
            pass
    
    @property
    def OutOfCards(self):
        if (len(self.__deck) < 1):
            self.__outOfCards = True
            return True
        
        else:
            self.__outOfCards = False
            return False
        
    @property
    def NumberOfCardsLeft(self):
        return len(self.__deck)
    
    def AddCard(self, card):
        if isinstance(card, Card):
            self.__deck.append(card)
            pass
        
    def DrawCard(self):
        if self.OutOfCards:
            return False
        else:
            return self.__deck.pop(0)