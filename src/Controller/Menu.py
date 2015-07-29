'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
'''
import View.Menu as MenuView
from View import GlobalFunc
import Model.Credits

class MenuController(object):
    
    __mainMenuVisible = False
    __settingsVisible = False
    
    __menuView = None
    
    __masterController = None
    
    
    MAIN_MENU = 'mainmenu'
    SETTINGS_MENU = 'settingsmenu'
    
    def __init__(self, viewArea, masterController):
        self.__mainMenuVisible = False
        self.__settingsVisible = False
        self.__menuView = MenuView.Menu(viewArea, self)
        self.__masterController = masterController
        
    def DisplayBasicMenu(self, root):
        self.__menuView.AddMenuText(root)
        
    def OpenMenu(self, *args, **kwargs):
        self.__masterController.OpenMenu(args)
        
    def OpenMainMenu(self, event, root):
        GlobalFunc.RemoveAllChildren(root)
        self.__menuView.DisplayMenu(None)

    def SaveUsername(self, event):
        userName = event.widget.master.nametowidget(self.__menuView.USER_NAME_WRAPPER).nametowidget(MenuView.Menu.USER_NAME_FRAME).get()
        self.__player.Name = userName
    
    def StartNewGame(self, event=None):
        self.__masterController.StartNewGame(event)
        
    def Credits(self, *args, **kwargs):
        self.__masterController.ShowCredits()
        
    def ShowCredits(self):
        cred = Model.Credits.Credits()
        self.__menuView.ShowCredits(cred)
    
    def ShowSettings(self):
        self.__menuView.ShowSettings(self.__masterController.Settings)
        
    def MusicOn(self, frame):
        self.__masterController.Settings.Music = True
        self.__masterController.ShowSettings()
        
    def MusicOff(self, frame):
        self.__masterController.Settings.Music = False
        self.__masterController.ShowSettings()