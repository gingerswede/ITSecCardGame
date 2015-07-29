'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
@copyright: 2015 Emil Carlsson
@license: This program is distributed under the terms of the GNU General Public License
'''
import Tkinter as tk, pygame
from Tkconstants import NW, BOTH

from View import GlobalFunc
from Controller import Menu as MenuController, Game as GameController
from Model import Player, Settings
from Model.Sounds import Sounds as Sound


class MasterController(object):
    VIEW_AREA = "viewarea"
    BACKGROUND_COLOR = "chartreuse4"
    BACKGROUND_COLOR_CARD = "green4"
    DECK_COLOR = "purple4"
    RED = "red4"
    
    __viewArea = None
    __menuArea = None
    
    __menuController = None
    __gameController = None
    
    __root = None
    __player = None
    
    __mixer = None
    __sounds = None
    __settings = None
    
    def __init__(self, root):
        self.__player = Player.Player()
        
        self.__root = root
        
        self.__settings = Settings.Settings()
        
        self.__menuArea = tk.Frame(root, width=root.winfo_screenwidth())
        self.__menuArea.pack(anchor=NW)
        
        background = tk.Frame(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), background=self.BACKGROUND_COLOR)
        background.pack(fill=BOTH, expand=True, pady=5, padx=5)
        
        self.__viewArea = tk.Frame(background, background=self.BACKGROUND_COLOR)
        self.__viewArea.pack(pady=10, padx=10, fill=BOTH, expand=True)
        
        self.__menuController = MenuController.MenuController(self.__viewArea, self)
        self.__gameController = GameController.GameController(self.__viewArea, self.__player, self)
        
        self.__menuController.DisplayBasicMenu(self.__menuArea)
        
        root.bind('<Escape>', lambda e, root=self.__viewArea: self.OpenMenu(root))
        root.bind('<x>', lambda e:self.CloseApplication())
        
        self.__sounds = Sound()
        self.__mixer = pygame.mixer
        self.__mixer.init()
        
        self.OpenMenu()
        
    def ShowCredits(self, *args, **kwargs):
        self.__mixer.stop()
        
        if self.__settings.Music:
            sound = self.__mixer.Sound(self.__sounds.EndCredit)
            sound.play(loops=-1)
        
        self.__menuController.ShowCredits()
        
    def ShowSettings(self, *args, **kwargs):
        self.__mixer.stop()
        
        if self.__settings.Music:
            sound = self.__mixer.Sound(self.__sounds.MenuMusic)
            sound.play(loops=-1)
            
        self.__menuController.ShowSettings()
        
    def OpenMenu(self):
        self.__mixer.stop()
        
        if self.__settings.Music:
            sound = self.__mixer.Sound(self.__sounds.MenuMusic)
            sound.play(loops=-1)
        
        self.__menuController.OpenMainMenu(self.__viewArea)
        
    def StartNewGame(self):
        self.__mixer.stop()
        if self.__settings.Music:
            sound = self.__mixer.Sound(self.__sounds.GamePlayMusic)
            sound.play(loops=-1)
        
        self.__gameController.StartNewGame()
        
    def CloseApplication(self):
        GlobalFunc.CloseWindow(self.__root)
        
    @property
    def Settings(self):
        return self.__settings