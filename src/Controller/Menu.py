'''
Created on 22 jul 2015

@author: Emil
'''
import View
from View import GlobalFunc
import Model.Credits

class MenuController(object):
    
    __mainMenuVisible = False
    __settingsVisible = False
    
    __menuView = None
    __player = None
    
    __masterController = None
    
    
    MAIN_MENU = 'mainmenu'
    SETTINGS_MENU = 'settingsmenu'
    
    def __init__(self, viewArea, player, masterController):
        self.__mainMenuVisible = False
        self.__settingsVisible = False
        self.__menuView = View.Menu.Menu(viewArea, self)
        self.__player = player
        self.__masterController = masterController
        
    def DisplayBasicMenu(self, root):
        self.__menuView.AddMenuText(root)
        
    def OpenMenu(self, *args, **kwargs):
        self.__masterController.OpenMenu(args)
        
    def OpenMainMenu(self, event, root):
        GlobalFunc.RemoveAllChildren(root)
        self.__menuView.DisplayMenu(None)

    def SaveUsername(self, event):
        userName = event.widget.master.nametowidget(self.__menuView.USER_NAME_WRAPPER).nametowidget(View.Menu.Menu.USER_NAME_FRAME).get()
        self.__player.Name = userName
    
    def StartNewGame(self, event=None):
        self.__masterController.StartNewGame(event)
        
    def Credits(self, *args, **kwargs):
        self.__masterController.ShowCredits()
        
    def ShowCredits(self):
        credits = Model.Credits.Credits()
        self.__menuView.ShowCredits(credits)
    
    def ShowSettings(self):
        self.__menuView.ShowSettings(self.__masterController.Settings)
        
    def MusicOn(self, frame):
        self.__masterController.Settings.Music = True
        self.__masterController.ShowSettings()
        
    def MusicOff(self, frame):
        self.__masterController.Settings.Music = False
        self.__masterController.ShowSettings()