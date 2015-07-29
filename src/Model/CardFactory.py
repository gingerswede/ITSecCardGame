'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
'''
from Model import DAL, Card, Deck
import random

class CardFactory(object):

    __dal = None
    def __init__(self, *args, **kwargs):
        self.__dal = DAL.DAL()
        
    def GetDeck(self, size=9):
        cards = self.__dal.GetAllCards()
        cardsForDeck = []
        
        for i in range(0, size):
            index = random.randint(0, len(cards) - 1)
            cardDb = cards[index]
            cardAp = random.randint(cardDb[self.__dal.CARDS_MIN_AP], cardDb[self.__dal.CARDS_MAX_AP])
            cardDp = random.randint(cardDb[self.__dal.CARDS_MIN_DP], cardDb[self.__dal.CARDS_MAX_DP])
            cardHp = random.randint(cardDb[self.__dal.CARDS_MIN_HP], cardDb[self.__dal.CARDS_MAX_HP])
            cardName = cardDb[self.__dal.CARDS_NAME]
            cardDescription = cardDb[self.__dal.CARDS_DESCRIPTION]
            cardImage = cardDb[self.__dal.CARDS_IMAGE]
            
            card = Card.Card(cardName, cardDescription, cardImage, cardAp, cardDp, cardHp)
            
            cardsForDeck.append(card)
            
        deck = Deck.Deck(deck=cardsForDeck)
        
        return deck