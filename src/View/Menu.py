'''
Created on 22 jul 2015

@author: Emil
'''
import Tkinter as tk
from PIL import Image, ImageTk
from Tkconstants import LEFT, X, CENTER, RIDGE, N, RIGHT, W, E
from tkFont import BOLD
import tkFont
from View import GlobalFunc

class Menu(object):
    START_GAME = "Start new game"
    SETTINGS = "Settings"
    MENU_HEADING = "Menu"
    INFO_MENU = "Menu (Esc)"
    INFO_EXIT = "Exit (x)"
    EXIT = "Exit"
    BACK = "Back"
    
    USER_NAME_FRAME = "usrNm"
    USER_NAME_WRAPPER = "usrNmWrp"
    
    FRAME_SETTING = "menu_settings"
    FRAME_ROOT = "menu_root"
    FRAME_START_GAME = "menu_start_game"
    FRAME_AI_SETTING = "menu_ai_setting"
    
    __root = None
    __controller = None
    
    def __init__(self, root, controller, *args, **kwargs):
        self.__root = root
        self.__controller = controller
    
    def DisplayMenu(self, event=None):
            
        GlobalFunc.RemoveAllChildren(self.__root)
            
        menuFrame = tk.Frame(self.__root)
        menuFrame.config(borderwidth=5, relief=RIDGE, background="red4")
        menuFrame.pack(anchor=CENTER)
            
        labelMenu = tk.Label(menuFrame, text=self.MENU_HEADING, background="red4")
        labelMenu.config(font=("Arial Black", 25, BOLD))
            
        menuFont = tkFont.Font(labelMenu, labelMenu.cget("font"))
        menuFont.configure(underline=True)
        labelMenu.config(font=menuFont)
        labelMenu.pack(fill=X, padx=10, pady=5)
            
        labelNewGame = tk.Label(menuFrame, text=self.START_GAME, background="red4")
        labelNewGame.config(font=("Arial Black", 20, BOLD))
        labelNewGame.bind("<Button-1>", lambda e:self.__controller.StartNewGame(e))
        labelNewGame.pack(fill=X, padx=10)
            
        labelSettings = tk.Label(menuFrame, text=self.SETTINGS, background="red4")
        labelSettings.config(font=("Arial Black", 20, BOLD))
        labelSettings.bind("<Button-1>", lambda e:self.ShowSettings(e))
        labelSettings.pack(fill=X, padx=10)
            
        labelExit = tk.Label(menuFrame, text=self.EXIT, background="red4")
        labelExit.config(font=("Arial Black", 20, BOLD))
        labelExit.bind("<Button-1>", lambda e, root = self.__root:GlobalFunc.CloseWindow(e, root))
        labelExit.pack(fill=X, padx=10)
    
    def AddMenuText(self, menuArea):
        
        label = tk.Label(menuArea, text=self.INFO_MENU, justify=LEFT)
        label.bind("<Button-1>", self.DisplayMenu)
        label.pack(side=LEFT, padx=5)
        
        labelClose = tk.Label(menuArea, text=self.INFO_EXIT, justify=LEFT)
        labelClose.bind("<Button-1>", lambda e, root=self.__root: GlobalFunc.CloseWindow(e, root))
        labelClose.pack()
        
    def ShowSettings(self, event):
        self.__menuVisible = False
        GlobalFunc.RemoveAllChildren(self.__root)
        
        settings = tk.Frame(self.__root)
        settings.config(borderwidth=5, relief=RIDGE, background="red4")
        settings.pack(anchor=CENTER)
        
        settingsHeading = tk.Label(settings, text=self.SETTINGS, background="red4")
        settingsHeading.config(font=("Arial Black", 25, BOLD))
            
        settingsFont = tkFont.Font(settingsHeading, settingsHeading.cget("font"))
        settingsFont.configure(underline=True)
        settingsHeading.config(font=settingsFont)
        
        settingsHeading.pack()
        
        usernameWrap = tk.Frame(settings, name=self.USER_NAME_WRAPPER, background="red4")
        usernameWrap.pack(anchor=N)
        
        userNameLabel = tk.Label(usernameWrap, text="Name: ", anchor=W, justify=RIGHT, background="red4")
        userNameLabel.config(font=("Arial Black", 20, BOLD))
        userNameLabel.pack(pady=2, padx=3, side=LEFT)
                
        userNameEntry = tk.Entry(usernameWrap, name=self.USER_NAME_FRAME, text="")
        userNameEntry.config(font=("Arial Black", 18))
        userNameEntry.pack(anchor=E, side=LEFT, padx=5)
        
        saveButton = tk.Button(settings, text="Save")
        saveButton.bind("<Button-1>", self.__controller.SaveUsername)
        saveButton.config(font=("Arial Black", 14), width=10)
        saveButton.pack(padx=5, pady=5)
        
        labelBack = tk.Label(settings, text=self.BACK, background="red4")
        labelBack.config(font=("Arial Black", 16, BOLD))
        labelBack.bind("<Button-1>", self.DisplayMenu)
        labelBack.pack(fill=X)