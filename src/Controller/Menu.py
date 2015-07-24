'''
Created on 22 jul 2015

@author: Emil
'''
import View
from View import GlobalFunc

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
        
    def OpenMainMenu(self, event, root):
        GlobalFunc.RemoveAllChildren(root)
        self.__menuView.DisplayMenu(None)

    def SaveUsername(self, event):
        userName = event.widget.master.nametowidget(self.__menuView.USER_NAME_WRAPPER).nametowidget(View.Menu.Menu.USER_NAME_FRAME).get()
        self.__player.Name = userName
    
    def StartNewGame(self, event=None):
        self.__masterController.StartNewGame(event)