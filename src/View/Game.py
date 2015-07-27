'''
Created on 24 jul 2015

@author: Emil
'''
from View import GlobalFunc
from View.Board import Board
from Tkconstants import BOTH, RIDGE

import Tkinter as tk
import Controller

class GameView(object):
    
    __root = None
    __controller = None
    
    __boardView = None
    
    def __init__(self, root, gameController, *args, **kwargs):
        self.__root = root
        self.__controller = gameController
        
    def StartNewGame(self, event=None, player=None, opponent=None):
        GlobalFunc.RemoveAllChildren(self.__root)
        self.__boardView = Board(self.__root, self.__controller, player, opponent)
        
    def OutOfMoves(self):
        self.__boardView.AddInformation("You are out of moves.\nPlease finnish your turn.")
        
    def ResetInformation(self):
        self.__boardView.ResetInformation()
        
    def MaxHandSize(self):
        self.__boardView.AddInformation("Maximum hand size reached.\nPlease play a card if possible.")
        
    def RefreshBoard(self, playerOne, playerTwo):
        self.__boardView.RefreshBoard(playerOne, playerTwo)            
        
    def RemoveFrame(self, frame):
        frame.destroy()
        
    def CardNotInHand(self):
        self.__boardView.AddInformation("Card not on your hand.")