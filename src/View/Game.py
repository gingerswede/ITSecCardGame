'''
Created on 24 jul 2015

@author: Emil
'''
from View import GlobalFunc
from View.Board import Board
from Tkconstants import BOTH

class GameView(object):
    
    __root = None
    __controller = None
    
    __boardView = None
    
    def __init__(self, root, gameController, *args, **kwargs):
        self.__root = root
        self.__controller = gameController
        
    def StartNewGame(self, event=None):
        GlobalFunc.RemoveAllChildren(self.__root)
        self.__boardView = Board(self.__root, self.__controller)