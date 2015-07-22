'''
Created on 21 jul 2015

@author: Emil
'''
import unittest
import random
from Model.Card import Card
from Model.Deck import Deck
from Model.Player import Player
from Model.Exceptions import IncorrectAttackerError, OutOfMovesError

class TestPlayer(unittest.TestCase):
    
    __handOne = None
    __handTwo = None
    __cardsHandOne = None
    __cardsHandTwo = None

    def setUp(self):
        cardsHandOne = [None] * 9
        cardsHandTwo = [None] * 9
        
        for i in range(0, 9):
            cardHandOne = Card("Card no %d" % i, "Card for hand one", "http://and.a.link/", random.randint(6,9), random.randint(2,3), random.randint(3,7))
            cardHandTwo = Card("Card no %d" % i, "Card for hand one", "http://and.a.link/", random.randint(4,7), random.randint(3,5), random.randint(3,7))
            
            cardsHandOne[i] = cardHandOne
            cardsHandTwo[i] = cardHandTwo
        
        self.__cardsHandOne = Deck(deck=cardsHandOne)
        self.__cardsHandTwo = Deck(deck=cardsHandTwo)
        
        self.__handOne = Player(name="Player one", deck=Deck(deck=cardsHandOne))
        self.__handTwo = Player(name="Player two", deck=Deck(deck=cardsHandTwo))
            
    def tearDown(self):
        self.__handOne = None
        self.__handTwo = None

    def testVisibleCards(self):
        visibleCards = []
        
        for i in range(0,3):
            self.__handOne.DrawCard()
            self.__handOne.EndTurn()
            self.__handOne.PutCard(self.__handOne.hand[0])
            visibleCards.append(self.__cardsHandOne.DrawCard())
            
            self.__handOne.EndTurn()
            self.__handTwo.EndTurn()
            
        expected = len(visibleCards)
        actual = len(self.__handOne.VisibleCards)
            
        self.assertEqual(expected, actual, "Visible card count is incorrect")
        
        for i in range(0,1):
            message = "Card %d is incorrect." % i
            self.assertEquals(visibleCards[i], self.__handOne.VisibleCards[i], message)
        
    def testPutCard(self):
        self.__handOne.DrawCard()
        self.__handOne.EndTurn()
        self.__handOne.PutCard(self.__handOne.hand[0])
        card = self.__handOne.VisibleCards[0]
        
        self.assertNotEquals(None, card, "PutCard() returns none")
        
        self.assertEquals(self.__cardsHandOne.DrawCard(), card, "PutCard did not take first card in deck")
    
    def testActionPoints(self):
        expectedStart = Player.MAX_ACTION_POINTS
        expectedAfterPutCard = expectedStart - Player.CARD_COST
        
        self.assertEqual(expectedStart, self.__handOne.ActionPoints, "Not correct number of ActionPoints at start")
              
        self.__handOne.DrawCard()
        
        self.assertEqual(expectedAfterPutCard, self.__handOne.ActionPoints, "Not correct number of ActionPoints after PutCard")
        
        self.__handOne.EndTurn()
        
        self.assertEqual(expectedStart, self.__handOne.ActionPoints, "ActionPoints not reset after end of turn")
    
    def testCardsLeft(self):
        expected = 9
        
        self.assertEqual(expected, self.__handOne.CardsLeft, "Number of cards left not displayed correct")
        
        expected = 7
        
        self.__handOne.DrawCard()
        self.__handOne.EndTurn()
        
        self.__handOne.PutCard(self.__handOne.hand[0])
        self.__handOne.EndTurn()
        self.__handOne.DrawCard()
        self.__handOne.EndTurn()
        self.__handOne.PutCard(self.__handOne.hand[0])
        
        self.assertEqual(expected, self.__handOne.CardsLeft, "Number of cards left not decreased correct")
        
    def testBattleSequence(self):
        expected = None
        
        self.__handOne.DrawCard()
        self.__handOne.EndTurn()
        self.__handOne.PutCard(self.__handOne.hand[0])
        self.__handOne.EndTurn()
        
        self.__handTwo.DrawCard()
        self.__handTwo.EndTurn()
        self.__handTwo.PutCard(self.__handTwo.hand[0])
        self.__handTwo.EndTurn()
        
        if self.__handOne.VisibleCards[0].AP > self.__handTwo.VisibleCards[0].DP:
            expected = self.__handOne.VisibleCards[0]
        else:
            expected = self.__handTwo.VisibleCards[0]
            
        actual = self.__handOne.Attack(self.__handTwo.VisibleCards[0], self.__handOne.VisibleCards[0])
        
        self.assertEquals(expected, actual, "Wrong winner on Player.Attack")
        
        try:
            self.__handOne.Attack(self.__handOne.VisibleCards[0], self.__handTwo.VisibleCards[0])
            self.fail("Attack with opponents card possible")
        except Exception, e:
            if isinstance(e, IncorrectAttackerError):
                self.__handOne.Attack(self.__handTwo.VisibleCards[0], self.__handOne.VisibleCards[0])
                self.__handOne.Attack(self.__handTwo.VisibleCards[0], self.__handOne.VisibleCards[0])
                
                try:
                    self.__handOne.Attack(self.__handTwo.VisibleCards[0], self.__handOne.VisibleCards[0])
                    self.fail("More attacks than AP allow possible")
                except Exception, e2:
                    if isinstance(e2, OutOfMovesError):
                        pass
                    else:
                        self.fail("Not correct error (OutOfMovesError)")
                    
            else:
                self.fail("Not correct error (IncorrectAttackerError)")
                
    def testDeadCard(self):
        self.__handOne.DrawCard()
        self.__handOne.EndTurn()
        self.__handOne.PutCard(self.__handOne.hand[0])
        
        self.__handTwo.DrawCard()
        self.__handTwo.EndTurn()
        self.__handTwo.PutCard(self.__handTwo.hand[0])
        
        self.__handOne.EndTurn()
        self.__handTwo.EndTurn()
        
        count = 0
                
        while self.__handOne.VisibleCards[0].IsAlive and self.__handTwo.VisibleCards[0].IsAlive:
            self.__handOne.Attack(self.__handTwo.VisibleCards[0], self.__handOne.VisibleCards[0])
            self.__handOne.EndTurn()
            self.__handTwo.EndTurn()
            count += 1
            if count > 100:
                self.fail("To many loops for battle simulation (DeadCard)")
                break
        
        self.__handOne.ClearBoard()
        self.__handTwo.ClearBoard()
        
        self.assertNotEqual(len(self.__handOne.VisibleCards), len(self.__handTwo.VisibleCards), "Card not removed on death")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()