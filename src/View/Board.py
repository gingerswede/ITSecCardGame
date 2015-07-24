'''
Created on 22 jul 2015

@author: Emil
'''
import Tkinter as tk
import tkFont

from Tkconstants import BOTH, RIDGE, LEFT, FLAT, RIGHT, N, NE, SUNKEN, S

import Controller

class Board(object):
    
    CARD_SPOT = "crdspt"
    DECK_SPOT = "dckspt"
    PLAYER_INFO_SPOT = "plrnfspt"
    PLAYER_NAME_INFO_SPOT = "plrnmspt"
    PLAYER_ACTION_POINTS_INFO_SPOT = "plrapspt"
    PLAYER_CARDS_LEFT_INFO_SPOT = "plrcrdlftspt"
    INPUT = "_inpt"
    
    PLAYER_INFO_HEADING = "Player information"
    PLAYER_INFO_PLAYER_NAME = "Player name:"
    PLAYER_INFO_ACTION_POINTS = "Action points:"
    PLAYER_INFO_CARDS_LEFT = "Cards left:"
    
    __root = None
    __controller = None
    
    __gameAreaPlayerOne = None
    __gameAreaPlayerTwo = None
    
    def __init__(self, root, controller):
        self.__root = root
        self.__controller = controller
        
        self.__gameAreaPlayerOne = tk.Frame(self.__root, background=Controller.Master.MasterController.BACKGROUND_COLOR, height=(self.__root.winfo_height()/2))
        self.__gameAreaPlayerTwo = tk.Frame(self.__root, background=Controller.Master.MasterController.BACKGROUND_COLOR, height=(self.__root.winfo_height()/2))
        
        self.__gameAreaPlayerTwo.pack(fill=BOTH)
        self.__gameAreaPlayerOne.pack(fill=BOTH)
        
        self.FillGameArea(self.__gameAreaPlayerOne)
        self.FillGameArea(self.__gameAreaPlayerTwo)
        
    def FillGameArea(self, gameArea):
        cardHeight = (self.__root.winfo_height()/2)*0.65
        cardWidth = (self.__root.winfo_width()/2)*0.25
        pady = ((self.__root.winfo_height()/2) - cardHeight)/2
        
        playerInfoWidth = self.__root.winfo_width() - (cardWidth*6)
        
        for i in range(0,5):
            cardSpot = tk.Frame(gameArea, name=self.CARD_SPOT+str(i), height=cardHeight, width=cardWidth)
            cardSpot.config(borderwidth=5, relief=RIDGE, background=Controller.Master.MasterController.BACKGROUND_COLOR)
            cardSpot.pack(side=LEFT, pady=pady, padx=10)
            cardSpot.bind("<Enter>", lambda e, area=cardSpot:self.MouseEnterArea(e, area))
            cardSpot.bind("<Leave>", lambda e, area=cardSpot:self.MouseLeaveArea(e, area))
            
        deckSpot = tk.Frame(gameArea, name=self.DECK_SPOT, height=cardHeight, width=cardWidth)
        deckSpot.config(borderwidth=5, relief=RIDGE, background=Controller.Master.MasterController.DECK_COLOR)
        deckSpot.pack(side=LEFT, padx=25, pady=pady)
        deckSpot.bind("<Enter>", lambda e, area=deckSpot:self.MouseEnterArea(e, area))
        deckSpot.bind("<Leave>", lambda e, area=deckSpot:self.MouseLeaveArea(e, area))
        
        playerInfoSpot = tk.Frame(gameArea, name=self.PLAYER_INFO_SPOT, width=playerInfoWidth, height=cardHeight)
        playerInfoSpot.config(background=Controller.Master.MasterController.BACKGROUND_COLOR, borderwidth=3)
        playerInfoSpot.pack(side=RIGHT, padx=25, pady=pady)
        
        self.GenerateTextPair(self.PLAYER_INFO_PLAYER_NAME, self.PLAYER_NAME_INFO_SPOT, playerInfoSpot)
        self.GenerateTextPair(self.PLAYER_INFO_ACTION_POINTS, self.PLAYER_ACTION_POINTS_INFO_SPOT, playerInfoSpot)
        self.GenerateTextPair(self.PLAYER_INFO_CARDS_LEFT, self.PLAYER_CARDS_LEFT_INFO_SPOT, playerInfoSpot)
        
        endTurnButton = tk.Button(playerInfoSpot, text="End turn")
        endTurnButton.pack(anchor=S, pady=25)
        
    def MouseEnterArea(self, event, area):
        area.config(relief=SUNKEN)
        
    def MouseLeaveArea(self, event, area):
        area.config(relief=RIDGE)
        
    def GenerateTextPair(self, text, textArea, root):
        wrapper = tk.Frame(root, name=textArea, background=Controller.Master.MasterController.BACKGROUND_COLOR)
        wrapper.pack(fill=BOTH)
        
        label = tk.Label(wrapper, text=text)
        label.config(font=("Arial Black", 10), background=Controller.Master.MasterController.BACKGROUND_COLOR)
        label.pack(side=LEFT)
        
        text = tk.Label(wrapper, name=textArea+self.INPUT, text="Placeholder")
        text.config(font=("Arial Black", 10, tkFont.BOLD), background=Controller.Master.MasterController.BACKGROUND_COLOR)
        text.pack(side=LEFT)