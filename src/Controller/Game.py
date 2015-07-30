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
from Model.Actions import Actions
import time

class GameController(object):
    
    __root = None
    __playerOne = None
    __playerTwo = None
    __ai = None
    __actionMessages = None
    
    __masterController = None
    __gameView = None
    __cardFactory = None
    __sounds = None
    
    __attacker = None
    __defender = None
    
    __imgPath = None
    __delay = 2
    
    __actionWinner = "winner"
    __actionAttacker = "attacker"
    __actionDefender = "defender"
    __actionCard = "card"
    
    ATTACK_CARD = "%s attacked %s.\n%s\n---"
    DRAW_CARD = "Your opponent drew a new card.\n---"
    PLACE_CARD = "Your opponent placed the card %s.\n---"
    PASS = "Your opponent passed this turn."
    
    def __init__(self, root, player, masterController):
        self.__root = root
        self.__playerOne = player
        self.__masterController = masterController
        self.__gameView = GameView.GameView(root, self)
        self.__imgPath = os.path.join(os.path.abspath(os.getcwd()), "..", "img")
        self.__sounds = Sound()
        self.__cardFactory = CardFactory()
        self.__actionMessages = []
        
    def StartNewGame(self):
        p1d = self.__cardFactory.GetDeck(10)
        p1d.Shuffle()
        p2d = self.__cardFactory.GetDeck(10)
        p2d.Shuffle()
        
        self.PlaySound(self.__sounds.Shuffle)
        
        self.__playerOne = Model.Player.Player(deck=p1d)
        self.__playerTwo = Model.Player.Player(deck=p2d)
        self.__gameView.StartNewGame(self.__playerOne, self.__playerTwo)
        self.__ai = AI.AI(self.__playerTwo, self)
        
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
        self.__gameView.WaitingForOpponent()

        self.__playerOne.EndTurn()
        self.__ai.MakeMove(self.__playerOne)
        self.__playerOne.ClearBoard()
        self.__playerTwo.ClearBoard()
        self.__gameView.RefreshBoard(self.__playerOne, self.__playerTwo)
        self.__gameView.ResetInformation()
        
        for message in self.__actionMessages:
            time.sleep(self.__delay)
            self.__gameView.AppendMessage(message)
            
        self.__gameView.AppendMessage("Your turn!")
            
        self.__actionMessages = []
        
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
            self.__playerOne.ClearBoard()
            self.__playerTwo.ClearBoard()
            self.__gameView.RefreshBoard(self.__playerOne, self.__playerTwo)
                
            self.__attacker = None
            self.__defender = None
            
        except OutOfMovesError:
            self.__gameView.OutOfMoves()
            
    def AddAction(self, action, *args, **kwargs):
        if action == Actions.ATTACK:
            winner = None
            if kwargs[self.__actionWinner].Name in self.__playerOne.VisibleCards:
                winner = "Your %s won." % kwargs[self.__actionWinner].Name
            else:
                winner = "Opponents %s won." % kwargs[self.__actionWinner].Name
            self.__actionMessages.append(self.ATTACK_CARD % (kwargs[self.__actionAttacker].Name, kwargs[self.__actionDefender].Name, winner))
        elif action == Actions.DRAW_CARD:
            self.__actionMessages.append(self.DRAW_CARD)
        elif action == Actions.PLACE_CARD:
            self.__actionMessages.append(self.PLACE_CARD % (kwargs[self.__actionCard].Name))
        elif action == Actions.PASS:
            self.__actionMessages.append(self.PASS)
            