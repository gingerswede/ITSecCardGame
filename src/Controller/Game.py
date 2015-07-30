'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
@copyright: 2015 Emil Carlsson
@license: This program is distributed under the terms of the GNU General Public License
'''

import Model, os

from View import Game as GameView
from Model.Exceptions import OutOfMovesError, MaxHandSize, CardNotInHand, MaxVisibleHandSize
from Model.Sounds import Sounds as Sound
from pygame import mixer
import Controller.AI as AI
from Model.CardFactory import CardFactory

class GameController(object):
    
    __root = None
    __playerOne = None
    __playerTwo = None
    __ai = None
    
    __cardFactory = None
    
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
        self.__cardFactory = CardFactory()
        
    def StartNewGame(self):
        
        
        p1d = self.__cardFactory.GetDeck(10)
        p1d.Shuffle()
        p2d = self.__cardFactory.GetDeck(10)
        p2d.Shuffle()
        
        self.PlaySound(self.__sounds.Shuffle)
        
        self.__playerOne = Model.Player.Player(deck=p1d)
        self.__playerTwo = Model.Player.Player(deck=p2d)
        self.__gameView.StartNewGame(self.__playerOne, self.__playerTwo)
        self.__ai = AI.AI(self.__playerTwo)
        
    def DisplayCardInfo(self, card):
        self.__gameView.DisplayCardInfo(card)
        
    def SetAttackerDefender(self, card):
        self.PlaySound(self.__sounds.Click)
        if card in self.__playerOne.VisibleCards:
            self.__attacker = card
        elif card in self.__playerTwo.VisibleCards:
            self.__defender = card
            
        if self.__attacker is not None and self.__defender is not None:
            self.PerformBattle()
            
    def DrawCard(self):
        try:
            self.__playerOne.DrawCard()
            self.PlaySound(self.__sounds.CardFlip)
            self.__gameView.RefreshBoard(self.__playerOne, self.__playerTwo)
        except OutOfMovesError:
            if self.__playerOne.CardsLeft == 0:
                self.__gameView.OutOfCards()
            else:
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
        
        if self.__playerOne.CardsLeft == 0 and len(self.__playerOne.hand) == 0 and len(self.__playerOne.VisibleCards) == 0:
            self.__gameView.PlayerLost()
        elif self.__playerTwo.CardsLeft == 0 and len(self.__playerTwo.hand) == 0 and len(self.__playerTwo.VisibleCards) == 0:
            self.__gameView.PlayerWon()
            
    def PlayCard(self, card):
        try:
            if card in self.__playerOne.hand:
                self.__playerOne.PutCard(card)
                self.PlaySound(self.__sounds.CardPlace)
                self.__gameView.RefreshBoard(self.__playerOne, self.__playerTwo)
                self.__gameView.ResetInformation()
            elif card in self.__playerOne.VisibleCards or card in self.__playerTwo.VisibleCards:
                self.SetAttackerDefender(card)
        except OutOfMovesError:
            self.__gameView.OutOfMoves()
        except CardNotInHand:
            self.__gameView.CardNotInHand()
        except MaxVisibleHandSize:
            self.__gameView.MaxVisibleHandSize()
    
    def PerformBattle(self):
        try:
            self.__playerOne.Attack(self.__defender, self.__attacker)
            
            self.__gameView.RefreshBoard(self.__playerOne, self.__playerTwo)
                
            self.__attacker = None
            self.__defender = None
            
        except OutOfMovesError:
            self.__gameView.OutOfMoves()