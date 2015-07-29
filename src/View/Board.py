'''
Created on 22 jul 2015

@author: Emil
'''
import Tkinter as tk
import tkFont

from Tkconstants import BOTH, RIDGE, LEFT, RIGHT, SUNKEN, S, NONE

import Controller
from View import GlobalFunc
from View.Card import Card
from tkFont import BOLD

class Board(object):
    PLAYER_INFO_HEADING = "Player information"
    PLAYER_INFO_PLAYER_NAME = "Player name:"
    PLAYER_INFO_ACTION_POINTS = "Action points:"
    PLAYER_INFO_CARDS_LEFT = "Cards left:"
    
    __root = None
    __controller = None
    
    __cardAreaPlayerOne = None
    __cardAreaPlayerTwo = None
    
    __handArea = None
    __handCardArea = None
    __messageArea = None
    __handDeckArea = None
    __playerInformationArea = None
    __visibleCardsArea = None
    
    __cardHeight = None
    __cardWidth = None
    __playerInfoWidth = None
    
    
    def __init__(self, root, controller, player, opponent):
        GlobalFunc.RemoveAllChildren(root)
        self.__root = root
        self.__controller = controller
        
        self.__cardHeight = 275
        self.__cardWidth = 190
        self.__playerInfoWidth = self.__root.winfo_width() - (self.__cardWidth*6)
        
        self.__visibleCardsArea = tk.Frame(self.__root, width=self.__root.winfo_width(), height=(self.__root.winfo_height()/3)*2, background=Controller.Master.MasterController.BACKGROUND_COLOR)
        self.__visibleCardsArea.grid(row=0)
        
        #Visible cards player one
        self.__cardAreaPlayerOne = tk.Frame(self.__visibleCardsArea, background=Controller.Master.MasterController.BACKGROUND_COLOR, width=((self.__root.winfo_width()-5)/4)*3, height=(self.__root.winfo_height()/3))
        #Visible cards player two
        self.__cardAreaPlayerTwo = tk.Frame(self.__visibleCardsArea, background=Controller.Master.MasterController.BACKGROUND_COLOR, width=((self.__root.winfo_width()-5)/4)*3, height=(self.__root.winfo_height()/3))
        
        #Messages
        self.__messageArea = tk.Frame(self.__visibleCardsArea, width=self.__root.winfo_width()/4, background=Controller.Master.MasterController.BACKGROUND_COLOR)
        
        self.__cardAreaPlayerTwo.grid(row=0, column=0)
        self.__cardAreaPlayerOne.grid(row=1, column=0)
        self.__messageArea.grid(row=0, column=1, rowspan=2)
             
        #Area with player information, deck, and cards on hand
        self.__handArea = tk.Frame(self.__root, background=Controller.Master.MasterController.BACKGROUND_COLOR, width=self.__root.winfo_width(), height=(self.__root.winfo_height()/3))
        self.__handArea.grid(row=1)
        
        #All cards on the hand not visible
        self.__handCardArea = tk.Frame(self.__handArea, height=self.__cardHeight, bg=Controller.Master.MasterController.BACKGROUND_COLOR)
        self.__handCardArea.pack(side=LEFT)
        
        #The purple square
        self.__handDeckArea = tk.Frame(self.__handArea , height=self.__cardHeight, width=self.__cardWidth)
        self.__handDeckArea.config(borderwidth=5, relief=RIDGE, background=Controller.Master.MasterController.DECK_COLOR)
        self.__handDeckArea.pack(side=LEFT, padx=25)
        self.__handDeckArea.bind("<Enter>", lambda e, area=self.__handDeckArea:self.MouseEnterArea(area))
        self.__handDeckArea.bind("<Leave>", lambda e, area=self.__handDeckArea:self.MouseLeaveArea(area))
        self.__handDeckArea.bind("<Button-1>", lambda e:self.__controller.DrawCard())
        
        #AP, Cards left, etc
        self.__playerInformationArea = tk.Frame(self.__handArea, width=self.__playerInfoWidth, height=self.__cardHeight)
        self.__playerInformationArea.pack(side=RIGHT)
        self.__playerInformationArea.config(background=Controller.Master.MasterController.BACKGROUND_COLOR, borderwidth=3)
        self.__playerInformationArea.pack(side=RIGHT, padx=25)
        
        self.DrawCards(self.__handCardArea, player.hand, player.MAX_HAND_SIZE)
        
        self.DrawCards(self.__cardAreaPlayerOne, player.VisibleCards, player.MAX_VISIBLE_CARDS)
        
        self.DrawCards(self.__cardAreaPlayerTwo, opponent.VisibleCards, opponent.MAX_VISIBLE_CARDS)
        
        self.PutPlayerInformation(player)
        
    def PutPlayerInformation(self, player):
        GlobalFunc.RemoveAllChildren(self.__playerInformationArea)
        self.GenerateTextPair(self.PLAYER_INFO_ACTION_POINTS, player.ActionPoints, self.__playerInformationArea)
        self.GenerateTextPair(self.PLAYER_INFO_CARDS_LEFT, player.CardsLeft, self.__playerInformationArea)
        
        endTurnButton = tk.Button(self.__playerInformationArea, text="End turn")
        endTurnButton.bind("<Button-1>", lambda e:self.__controller.EndTurn())
        endTurnButton.pack(anchor=S, pady=25)
        
    
    def DrawCards(self, frame, cards, maxFrames):
        GlobalFunc.RemoveAllChildren(frame)
        counter = 0
        for c in cards:
            cardSpot = tk.Frame(frame, height=self.__cardHeight, width=self.__cardWidth)
            cardSpot.config(borderwidth=5, relief=RIDGE)
            cardSpot.pack(side=LEFT, pady=10, padx=10, fill=NONE)
            cardSpot.pack_propagate(0)
            card = Card(c, self.__controller)
            card.Draw(cardSpot, self.__cardHeight, self.__cardWidth)
            
            cardSpot.bind("<Enter>", lambda e, area=cardSpot:self.MouseEnterArea(area))
            cardSpot.bind("<Leave>", lambda e, area=cardSpot:self.MouseLeaveArea(area))
            counter += 1
            
        if counter < maxFrames:
            for i in range(counter,maxFrames):
                cardSpot = tk.Frame(frame, height=self.__cardHeight, width=self.__cardWidth)
                cardSpot.config(borderwidth=5, relief=RIDGE, background=Controller.Master.MasterController.BACKGROUND_COLOR_CARD)
                cardSpot.pack(side=LEFT, pady=10, padx=10)
                cardSpot.bind("<Enter>", lambda e, area=cardSpot:self.MouseEnterArea(area))
                cardSpot.bind("<Leave>", lambda e, area=cardSpot:self.MouseLeaveArea(area))
                
    def RefreshBoard(self, playerOne, playerTwo):        
        self.DrawCards(self.__handCardArea, playerOne.hand, playerOne.MAX_HAND_SIZE)
        self.DrawCards(self.__cardAreaPlayerOne, playerOne.VisibleCards, playerOne.MAX_VISIBLE_CARDS)
        self.DrawCards(self.__cardAreaPlayerTwo, playerTwo.VisibleCards, playerTwo.MAX_VISIBLE_CARDS)
        
        self.PutPlayerInformation(playerOne)
        
    def AddInformation(self, informationText):
        GlobalFunc.RemoveAllChildren(self.__messageArea)
        information = tk.Frame(self.__messageArea, background=Controller.Master.MasterController.RED, borderwidth=5, relief=RIDGE)
        information.pack(fill=BOTH)
        label = tk.Label(information, text=informationText, background=Controller.Master.MasterController.RED, wraplength=(self.__root.winfo_width()/4)-10)
        label.config(font=("Arial Black", 16, BOLD))
        label.pack()
        
    def GenerateTextPair(self, text, value, root):
        wrapper = tk.Frame(root, background=Controller.Master.MasterController.BACKGROUND_COLOR)
        wrapper.pack(fill=BOTH)
        
        label = tk.Label(wrapper, text=text)
        label.config(font=("Arial Black", 10), background=Controller.Master.MasterController.BACKGROUND_COLOR)
        label.pack(side=LEFT)
        
        text = tk.Label(wrapper, text=value)
        text.config(font=("Arial Black", 10, tkFont.BOLD), background=Controller.Master.MasterController.BACKGROUND_COLOR)
        text.pack(side=LEFT)
        
    def MouseEnterArea(self, area):
        area.config(relief=SUNKEN)
        
    def MouseLeaveArea(self, area):
        area.config(relief=RIDGE)

    def RemoveFrame(self, frame):
        frame.destroy()
        
    def ResetInformation(self):
        GlobalFunc.RemoveAllChildren(self.__messageArea)
        self.__messageArea.config(background=Controller.Master.MasterController.BACKGROUND_COLOR)