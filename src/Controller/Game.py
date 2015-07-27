'''
Created on 22 jul 2015

@author: Emil
'''

import Model, random, os

from View import Game as GameView
from Model.Exceptions import OutOfMovesError, MaxHandSize, CardNotInHand
from Model.Deck import Deck
from Model.Card import Card

class GameController(object):
    
    __root = None
    __playerOne = None
    __playerTwo = None
    __ai = None
    
    __imgPath = None
    
    __masterController = None
    
    __gameView = None
    
    def __init__(self, root, player, masterController):
        self.__root = root
        self.__playerOne = player
        self.__masterController = masterController
        self.__gameView = GameView.GameView(root, self)
        self.__imgPath = os.path.join(os.path.abspath(os.getcwd()), "..", "img")
        print self.__imgPath
        
    def StartNewGame(self, event):
        #TODO! Fix before release
        cardsHandOne = [None] * 9
        cardsHandTwo = [None] * 9
        
        for i in range(0, 9):
            cardHandOne = Card("Card no %d" % i, "A firewall will give you defense against intruders by filtering by who and when a connection is allowed.", os.path.join(self.__imgPath, "firewall.jpg"), random.randint(6,9), random.randint(2,3), random.randint(3,7))
            cardHandTwo = Card("Card no %d" % i, "A firewall will give you defense against intruders by filtering by who and when a connection is allowed.", os.path.join(self.__imgPath, "firewall.jpg"), random.randint(4,7), random.randint(3,5), random.randint(3,7))
            
            cardsHandOne[i] = cardHandOne
            cardsHandTwo[i] = cardHandTwo
            
        p1d = Deck(deck=cardsHandOne)
        p1d.Shuffle()
            
        self.__playerOne = Model.Player.Player(deck=p1d)
        self.__playerTwo = Model.Player.Player(deck=Deck(deck=cardsHandTwo))
        self.__gameView.StartNewGame(event, self.__playerOne, self.__playerTwo)
        
    def DisplayCardInfo(self, event, card):
        self.__gameView.DisplayCardInfo(card)
        
    def SetAttackerDefender(self, card):
        if card in self.__playerOne.hand:
            self.__attacker = card
        elif card in self.__playerTwo.hand:
            self.__defender = card
            
        if self.__attacker is not None and self.__defender is not None:
            self.PerformBattle()
            
    def DrawCard(self):
        try:
            self.__playerOne.DrawCard()
            self.__gameView.RefreshBoard(self.__playerOne, self.__playerTwo)
        except OutOfMovesError:
            self.__gameView.OutOfMoves()
        except MaxHandSize:
            self.__gameView.MaxHandSize()
            
    def EndTurn(self):
        self.__playerOne.EndTurn()
        self.__gameView.RefreshBoard(self.__playerOne, self.__playerTwo)
        self.__gameView.ResetInformation()
        
    def PlayCard(self, card):
        try:
            self.__playerOne.PutCard(card)
            self.__gameView.RefreshBoard(self.__playerOne, self.__playerTwo)
            self.__gameView.ResetInformation()
        except OutOfMovesError:
            self.__gameView.OutOfMoves()
        except CardNotInHand:
            self.__gameView.CardNotInHand()    
    
    def PerformBattle(self):
        try:
            winner = self.__playerOne.Attack(self.__defender, self.__attacker)
            
            if winner == self.__attacker:
                self.__gameView.UpdateOpponentVisibleHand(self.__playerTwo.hand)
            else:
                self.__gameView.UpdateOwnVisibleHand(self.__playerOne.hand)
            
        except OutOfMovesError:
            self.__gameView.OutOfMoves()