'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
'''
import unittest
import Model.Card as Card
from Model.Deck import Deck

class TestDeck(unittest.TestCase):

    def testShuffle(self):
        cards = [None] * Deck.MINIMUM_DECK_SIZE
        shuffledCards = [None] * Deck.MAXIMUM_DECK_SIZE
        count = 0
        
        for i in range(0, Deck.MINIMUM_DECK_SIZE):
            cards[i] = Card.Card("Card %s" % str(i), "Card one Description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", 1, 1, 1)
        
        deck = Deck(deck=cards)
        deck.Shuffle()
        
        while not deck.OutOfCards:
            shuffledCards[count] = deck.DrawCard()
            count += 1
        
        different = 0
        for i in range(0, len(cards)):
            if cards[i].Name != shuffledCards[i].Name:
                different += 1
                
        errorMsg = "Deck not shuffled properly. Number of cards not changed placement: %d" % different
        
        self.assertFalse(different < 2, errorMsg)
        
        pass
    
    def testOutOfCards(self):
        deck = Deck()
        
        deck.AddCard(Card.Card("Card name", "Card one Description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", 1, 1, 1))
        
        self.assertFalse(deck.OutOfCards, "Deck with a card marked as out of cards")
        
        deck.DrawCard()
        
        self.assertTrue(deck.OutOfCards, "Deck with no cards marked as containing cards")
        
        pass
    
    def testAddCard(self):
        card = Card.Card("Card name", "Card one Description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", 1, 1, 1)
    
        deck = Deck()
        
        self.assertTrue(deck.OutOfCards, "Deck marked as containing cards with no cards")
        
        try:
            deck.AddCard(card)
            
        except:
            self.fail("Card was not added (AssertFail)")
            
        self.assertEquals(card, deck.DrawCard(), "Card not added correct")
        
    def testDrawCard(self):
        card = Card.Card("Card name", "Card one Description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", 1, 1, 1)
        deck = Deck()
        
        deck.AddCard(card)
        
        try:
            deck.DrawCard()
        except:
            self.fail("Card not drawn with one card in the deck")
            
        self.assertFalse(deck.DrawCard(), "Deck returned card and now false when deck is empty")
        
    def testNumberOfCardsLeft(self):
        card = Card.Card("Card name", "Card one Description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", 1, 1, 1)
        
        deck = Deck()
        
        deck.AddCard(card)
        
        self.assertEqual(1, deck.NumberOfCardsLeft, "Wrong number of cards left displayed")
        
        deck.AddCard(card)
        
        self.assertEqual(2, deck.NumberOfCardsLeft, "Wrong number of cards left displayed after card added")
        
        deck.DrawCard()
        
        self.assertEqual(1, deck.NumberOfCardsLeft, "Wrong number of cards left displayed after card removed")
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGenerate']
    unittest.main()