'''
Created on 22 jul 2015

@author: Emil
'''
from View import Game as GameView

class GameController(object):
    
    __root = None
    __player = None
    __ai = None
    
    __masterController = None
    
    __gameView = None
    
    def __init__(self, root, player, masterController):
        self.__root = root
        self.__player = player
        self.__masterController = masterController
        self.__gameView = GameView.GameView(root, self)
        
    def StartNewGame(self, event):
        self.__gameView.StartNewGame(event)