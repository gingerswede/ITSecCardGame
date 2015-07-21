'''
Created on 21 jul 2015

@author: Emil
'''
import unittest
import random
from Model.Card import Card
from Model.Deck import Deck
from Model.Player import Player

class TestPlayer(unittest.TestCase):
    
    __handOne = None
    __handTwo = None
    __cardsHandOne = None
    __cardsHandTwo = None

    def setUp(self):
        cardsHandOne = [None] * 9
        cardsHandTwo = [None] * 9
        
        for i in range(0, 9):
            cardHandOne = Card("Card no %d" % i, "Card for hand one", "http://and.a.link/", random.randint(4,7), random.randint(3,5), random.randint(3,7))
            cardHandTwo = Card("Card no %d" % i, "Card for hand one", "http://and.a.link/", random.randint(4,7), random.randint(3,5), random.randint(3,7))
            
            cardsHandOne[i] = cardHandOne
            cardsHandTwo[i] = cardHandTwo
        
        self.__cardsHandOne = Deck(deck=cardsHandOne)
        self.__cardsHandTwo = Deck(deck=cardsHandTwo)
        
        self.__handOne = Player(name="Player one", deck=Deck(cardsHandOne))
        self.__handTwo = Player(name="Player two", deck=Deck(cardsHandTwo))
            
    def tearDown(self):
        self.__handOne = None
        self.__handTwo = None

    def testVisibleCards(self):
        visibleCards = []
        
        for i in range(0,3):
            self.__handOne.PutCard()
            visibleCards.append(self.__handOne.DrawCard())
            self.__handTwo.PutCard()
        
        self.assertEqual(len(visibleCards), self.__handOne.VisibleCards, "Visible card count is incorrect")
        
        for i in range(0,1):
            message = "Card %d is incorrect." % str(i)
            self.assertEquals(visibleCards[i], self.__handOne.VisibleCards, message)
        
    def testPutCard(self):
        self.__handOne.PutCard()
        card = self.__handOne.VisibleCards[0]
        
        self.assertNotEquals(None, card, "PutCard() returns none")
        
        self.assertEquals(self.__cardsHandOne.DrawCard(), card, "PutCard did not take first card in deck")
    
    def testActionPoints(self):
        expectedStart = 3
        expectedAfterPutCard = 2
        
        self.assertEqual(expectedStart, self.__handOne.ActionPoints, "Not correct number of ActionPoints at start")
              
        self.__handOne.PutCard()
        
        self.assertEqual(expectedAfterPutCard, self.__handOne.ActionPoints, "Not correct number of ActionPoints after PutCard")
        
        self.__handOne.EndTurn()
        
        self.assertEqual(expectedStart, self.__handOne.ActionPoints, "ActionPoints not reset after end of turn")
    
    def testCardsLeft(self):
        expected = 9
        
        self.assertEqual(expected, self.__handOne.CardsLeft, "Number of cards left not displayed correct")
        
        expected = 7
        
        self.__handOne.PutCard()
        self.__handOne.PutCard()
        
        self.assertEqual(expected, self.__handOne.CardsLeft, "Number of cards left not decreased correct")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()