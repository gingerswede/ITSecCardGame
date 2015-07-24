'''
Created on 22 jul 2015

@author: Emil
'''
import Tkinter as tk
from Tkconstants import NW, BOTH

from View import Menu, GlobalFunc
from Controller import Menu as MenuController, Game as GameController
from Model import Player


class MasterController(object):
    VIEW_AREA = "viewarea"
    BACKGROUND_COLOR = "chartreuse4"
    DECK_COLOR = "purple4"
    
    __viewArea = None
    __menuArea = None
    
    __menuController = None
    __gameController = None
    
    __root = None
    __player = None
    
    def __init__(self, root):
        self.__player = Player.Player()
        
        self.__root = root
        
        self.__menuArea = tk.Frame(root, width=root.winfo_screenwidth())
        self.__menuArea.pack(anchor=NW)
        
        background = tk.Frame(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), background="chartreuse4")
        background.pack(fill=BOTH, expand=True, pady=5, padx=5)
        
        self.__viewArea = tk.Frame(background, background="chartreuse4")
        self.__viewArea.pack(pady=10, padx=10, fill=BOTH, expand=True)
        
        self.__menuController = MenuController.MenuController(self.__viewArea, self.__player, self)
        self.__gameController = GameController.GameController(self.__viewArea, self.__player, self)
        
        self.__menuController.DisplayBasicMenu(self.__menuArea)
        
        root.bind('<Escape>', lambda e, root=self.__viewArea: self.__menuController.OpenMainMenu(e, root))
        root.bind('<x>', self.CloseApplication)
        
        self.__menuController.OpenMainMenu(None, self.__viewArea)
        
    def StartNewGame(self, event):
        self.__gameController.StartNewGame(event)
        
    def CloseApplication(self, event=None):
        GlobalFunc.CloseWindow(event, self.__root)