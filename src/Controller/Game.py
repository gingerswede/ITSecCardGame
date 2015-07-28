'''
Created on 22 jul 2015

@author: Emil
'''

import Model, random, os

from View import Game as GameView
from Model.Exceptions import OutOfMovesError, MaxHandSize, CardNotInHand, MaxVisibleHandSize
from Model.Deck import Deck
from Model.Card import Card
from Model.Sounds import Sounds as Sound
from pygame import mixer
import Controller.AI as AI

class GameController(object):
    
    __root = None
    __playerOne = None
    __playerTwo = None
    __ai = None
    
    __attacker = None
    __defender = None
    
    __imgPath = None
    
    __masterController = None
    
    __gameView = None
    
    __sounds = None
    
    def __init__(self, root, player, masterController):
        self.__root = root
        self.__playerOne = player
        self.__masterController = masterController
        self.__gameView = GameView.GameView(root, self)
        self.__imgPath = os.path.join(os.path.abspath(os.getcwd()), "..", "img")
        self.__sounds = Sound()
        
    def StartNewGame(self, event):
        #TODO! Fix before release
        cardsHandOne = [None] * 9
        cardsHandTwo = [None] * 9
        
        for i in range(0, 9):
            cardHandOne = Card("Card no %d" % i, "A firewall will give you defense against intruders by filtering by who and when a connection is allowed.", os.path.join(self.__imgPath, "firewall.jpg"), random.randint(6,9), random.randint(6,9), random.randint(5,7))
            cardHandTwo = Card("Card no %d" % i, "A firewall will give you defense against intruders by filtering by who and when a connection is allowed.", os.path.join(self.__imgPath, "firewall.jpg"), random.randint(6,9), random.randint(6,9), random.randint(5,7))
            
            cardsHandOne[i] = cardHandOne
            cardsHandTwo[i] = cardHandTwo
            
        p1d = Deck(deck=cardsHandOne)
        p1d.Shuffle()
        p2d = Deck(deck=cardsHandTwo)
        p2d.Shuffle()
        
        self.PlaySound(self.__sounds.Shuffle)
        
        self.__playerOne = Model.Player.Player(deck=p1d)
        self.__playerTwo = Model.Player.Player(deck=p2d)
        self.__gameView.StartNewGame(event, self.__playerOne, self.__playerTwo)
        self.__ai = AI.AI(self.__playerTwo)
        
    def DisplayCardInfo(self, event, card):
        self.__gameView.DisplayCardInfo(card)
        
    def SetAttackerDefender(self, card):
        self.PlaySound(self.__sounds.Click)
        if card in self.__playerOne.hand:
            self.__attacker = card
        elif card in self.__playerTwo.hand:
            self.__defender = card
            
        if self.__attacker is not None and self.__defender is not None:
            self.PerformBattle()
            
    def DrawCard(self):
        try:
            self.__playerOne.DrawCard()
            self.PlaySound(self.__sounds.CardFlip)
            self.__gameView.RefreshBoard(self.__playerOne, self.__playerTwo)
        except OutOfMovesError:
            self.__gameView.OutOfMoves()
        except MaxHandSize:
            self.__gameView.MaxHandSize()
            
    def PlaySound(self, fileName):
        mixer.init()
        sound = mixer.Sound(fileName)
        sound.play()
            
    def EndTurn(self):
        self.__playerOne.EndTurn()
        self.__ai.MakeMove(self.__playerOne)
        self.__playerOne.ClearBoard()
        self.__playerTwo.ClearBoard()
        self.__gameView.RefreshBoard(self.__playerOne, self.__playerTwo)
        self.__gameView.ResetInformation()
        for c in self.__playerTwo.hand:
            print c.Name
        
    def PlayCard(self, card):
        try:
            if card in self.__playerOne.hand:
                self.__playerOne.PutCard(card)
                self.PlaySound(self.__sounds.CardPlace)
                self.__gameView.RefreshBoard(self.__playerOne, self.__playerTwo)
                self.__gameView.ResetInformation()
            elif card in self.__playerOne.VisibleCards:
                self.SetAttackerDefender(card)
        except OutOfMovesError:
            self.__gameView.OutOfMoves()
        except CardNotInHand:
            self.__gameView.CardNotInHand()
        except MaxVisibleHandSize:
            self.__gameView.MaxVisibleHandSize()
    
    def PerformBattle(self):
        try:
            winner = self.__playerOne.Attack(self.__defender, self.__attacker)
            
            if winner == self.__attacker:
                self.__gameView.UpdateOpponentVisibleHand(self.__playerTwo.hand)
            else:
                self.__gameView.UpdateOwnVisibleHand(self.__playerOne.hand)
                
            self.__attacker = None
            self.__defender = None
            
        except OutOfMovesError:
            self.__gameView.OutOfMoves()