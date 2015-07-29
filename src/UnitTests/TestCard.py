'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
'''
import unittest
from Model import Card


class TestCard(unittest.TestCase):


    def testCardSetAP(self):
        expected = 5        
        card = Card.Card("Card one", "Card one Description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", 1, 1, 1)
        try:
            card.AP = expected
    
            self.assertEqual(card.AP, expected, "card.AP not set correct (assert.equal)")
            
            try:
                card.AP = -4
                self.fail("AP able to be negative")
            except:
                pass
        except:
            self.fail("Card.AP not set correct (assert.fail)")
        pass
    
    def testCardSetHP(self):
        expected = 5        
        expectedDecrease = 3        
        card = Card.Card("Card one", "Card one Description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", 1, 1, 1)
        
        try:
            card.HP = expected
            
            self.assertEqual(card.HP, expected, "card.HP not set correct (Assert.Equal)")
            
            card.HP = card.HP - expectedDecrease
            expected = expected - expectedDecrease
                
            self.assertEqual(card.HP, expected, "card.HP not decreased correct")
            
            try:
                expected = -5
                card.HP = expected
                
                self.fail("card.HP able to be negative")
                
            except:
                pass
            
        except:
            self.fail("card.HP not set correct (Assert.Fail)")
        
        pass
            
    def testCardSetName(self):
        card = Card.Card("Card one", "Card one Description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", 1, 1, 1)
        expected = "Card name"
        
        try:
            card.name = expected
            
            self.assertEqual(card.name, expected, "Card.name not set correct (Assert.Equal)")
        except:
            self.fail("Card.name not set correct (Assert.Fail)")
            
        pass
            
    def testCardSetDP(self):
        card = Card.Card("Card one", "Card one Description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", 1, 1, 1)
        expected = 5
        
        try:
            card.DP = expected
            
            self.assertEqual(card.DP, expected, "Card.DP not set correct (Assert.Fail)")
        except:
            self.fail("Card.DP not set correct (Assert.Fail)")
            
        try:
            expected = -4
            card.DP = expected
            self.fail("Card.DP able to be set negative")
        except:
            pass
        
        pass
    
    def testCardBattle(self):
        cardOneAp = 5
        cardOneDp = 6
        cardOneHp = 4
        
        cardTwoAp = 4
        cardTwoDp = 4
        cardTwoHp = 7
        
        cardOne = Card.Card("Card one", "Card one Description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", cardOneAp, cardOneDp, cardOneHp)
        cardTwo = Card.Card("Card two", "Card two description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", cardTwoAp, cardTwoDp, cardTwoHp)
        
        expectedWinnerAttackOne = cardOne
        actualWinnerAttackOne = None
        
        try:
            actualWinnerAttackOne = cardTwo.defend(cardOne)
        except:
            self.fail("card.defend throw exception")
            
        self.assertEquals(expectedWinnerAttackOne, actualWinnerAttackOne, "Wrong card winner ap > dp")
        self.assertTrue(cardTwoHp > cardTwo.HP, "Hp not decreased correct ap > dp")
        
        newCardTwoHp = cardTwo.HP
        
        expectedWinnerAttackTwo = cardOne        
        actualWinnerAttackTwo = cardOne.defend(cardTwo)
        
        self.assertEquals(expectedWinnerAttackTwo, actualWinnerAttackTwo, "Wrong card winner dp > ap")
        
        self.assertTrue(newCardTwoHp > cardTwo.HP, "Hp not decreased correct dp > ap")
        
        pass
    
    def testKillCard(self):
        cardOneAp = 5
        cardOneDp = 6
        cardOneHp = 4
        
        cardTwoAp = 4
        cardTwoDp = 2
        cardTwoHp = 1
        
        cardOne = Card.Card("Card one", "Card one Description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", cardOneAp, cardOneDp, cardOneHp)
        cardTwo = Card.Card("Card two", "Card two description", "https://sv.wikipedia.org/wiki/Portal:Huvudsida#/media/File:Panama_Canal_Gatun_Locks.jpg", cardTwoAp, cardTwoDp, cardTwoHp)
        
        winner = cardTwo.defend(cardOne)
        
        self.assertEqual(winner, cardOne, "Wrong card won")
        
        self.assertLess(cardTwo.HP, 1, "Card two did not die")
        
        self.assertFalse(cardTwo.IsAlive, "Card two is marked as alive")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()