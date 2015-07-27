'''
Created on 22 jul 2015

@author: Emil
'''
import Tkinter as tk
import tkFont

from Tkconstants import BOTH, RIDGE, LEFT, FLAT, RIGHT, N, NE, SUNKEN, S, GROOVE, E, W, NW, SW

import Controller
from View import GlobalFunc
from View.Card import Card
from tkFont import BOLD
import Model

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
    
    __cardAreaPlayerOne = None
    __cardAreaPlayerTwo = None
    
    __handArea = None
    __handCardArea = None
    __informationArea = None
    __handDeckArea = None
    __playerInformationArea = None
    
    __cardHeight = None
    __cardWidth = None
    __playerInfoWidth = None
    
    
    def __init__(self, root, controller, player, opponent):
        GlobalFunc.RemoveAllChildren(root)
        self.__root = root
        self.__controller = controller
        
        self.__cardHeight = 230
        self.__cardWidth = 160
        self.__playerInfoWidth = self.__root.winfo_width() - (self.__cardWidth*6)
        
        cardArea = tk.Frame(self.__root, background=Controller.Master.MasterController.BACKGROUND_COLOR, height=(self.__root.winfo_height()/3)*2, width=self.__root.winfo_width())
        cardArea.pack()
        
        self.__cardAreaPlayerOne = tk.Frame(cardArea, background=Controller.Master.MasterController.BACKGROUND_COLOR, width=((self.__root.winfo_width()-5)/4)*3, height=(self.__root.winfo_height()/3))
        self.__cardAreaPlayerTwo = tk.Frame(cardArea, background=Controller.Master.MasterController.BACKGROUND_COLOR, width=((self.__root.winfo_width()-5)/4)*3, height=(self.__root.winfo_height()/3))
        infoArea = tk.Frame(cardArea, background=Controller.Master.MasterController.BACKGROUND_COLOR, width=((self.__root.winfo_width()-5)/4), height=(self.__root.winfo_height()/3)*2)
        infoArea.grid(row=0, column=1, rowspan=2)
        self.__informationArea = tk.Frame(infoArea)
             
        self.__cardAreaPlayerTwo.grid(row=0, column=0)
        self.__cardAreaPlayerOne.grid(row=1, column=0)
        self.__informationArea.grid(row=0, column=1, rowspan=2)
             
        self.__handArea = tk.Frame(self.__root, background=Controller.Master.MasterController.BACKGROUND_COLOR, width=self.__root.winfo_width(), height=(self.__root.winfo_height()/3))
        self.__handArea.pack(anchor=S)
        
        self.__handCardArea = tk.Frame(self.__handArea, height=self.__cardHeight, width=(self.__root.winfo_width()-(self.__playerInfoWidth+self.__cardWidth))-5, bg="red")
        self.__handCardArea.pack(side=LEFT)
        
        self.__handDeckArea = tk.Frame(self.__handArea, name=self.DECK_SPOT, height=self.__cardHeight, width=self.__cardWidth)
        self.__handDeckArea.config(borderwidth=5, relief=RIDGE, background=Controller.Master.MasterController.DECK_COLOR)
        self.__handDeckArea.pack(side=LEFT, padx=25)
        self.__handDeckArea.bind("<Enter>", lambda e, area=self.__handDeckArea:self.MouseEnterArea(area))
        self.__handDeckArea.bind("<Leave>", lambda e, area=self.__handDeckArea:self.MouseLeaveArea(area))
        self.__handDeckArea.bind("<Button-1>", lambda e:self.__controller.DrawCard())
        
        self.__playerInformationArea = tk.Frame(self.__handArea, name=self.PLAYER_INFO_SPOT, width=self.__playerInfoWidth, height=self.__cardHeight)
        self.__playerInformationArea.pack(side=RIGHT)
        self.__playerInformationArea.config(background=Controller.Master.MasterController.BACKGROUND_COLOR, borderwidth=3)
        self.__playerInformationArea.pack(side=RIGHT, padx=25)
        
        endTurnButton = tk.Button(self.__playerInformationArea, text="End turn")
        endTurnButton.bind("<Button-1>", lambda e:self.__controller.EndTurn())
        endTurnButton.pack(anchor=S, pady=25)
        
        self.FillHandArea(player)
        self.FillCardArea(self.__cardAreaPlayerOne, player)
        self.FillCardArea(self.__cardAreaPlayerTwo, opponent)
        
    def FillCardArea(self, root, player):
        GlobalFunc.RemoveAllChildren(root)
        
        pady = ((self.__root.winfo_height()/3) - self.__cardHeight)/2
        
        visibleCards = tk.Frame(root, background=Controller.Master.MasterController.BACKGROUND_COLOR)
        visibleCards.pack()
        
        self.PlaceVisibleCards(visibleCards, pady, player.VisibleCards)
        
    def FillHandArea(self, player):
        self.PopulateHand(player.hand)
                
        self.GenerateTextPair(self.PLAYER_INFO_ACTION_POINTS, player.ActionPoints, self.PLAYER_ACTION_POINTS_INFO_SPOT, self.__playerInformationArea)
        self.GenerateTextPair(self.PLAYER_INFO_CARDS_LEFT, player.CardsLeft, self.PLAYER_CARDS_LEFT_INFO_SPOT, self.__playerInformationArea)
        
    def PopulateHand(self, hand):
        GlobalFunc.RemoveAllChildren(self.__handCardArea)
        for c in hand:
            cardSpot = tk.Frame(self.__handCardArea, borderwidth=4, relief=GROOVE, height=self.__cardHeight, width=self.__cardWidth)
            cardSpot.pack(side=LEFT, padx=5)
            card = Card(c, self.__controller)
            card.Draw(cardSpot, self.__cardHeight, self.__cardWidth)
            
            cardSpot.bind("<Button-1>", lambda e, card=card:self.__controller.PlayCard(card))
    
    def DisplayCardInfo(self, card):
        padY = (self.__root.winfo_height()/3)
        padX = (self.__root.winfo_width()-padY*0.4)/2
        
        cardInfo = card.GenerateLarge(self.__root, padX, padY)
        
        cardInfo.bind("<Button-1>", lambda e, frame=cardInfo:self.RemoveFrame(frame))        
    
    def PlaceVisibleCards(self, root, paddingY, cards):
        GlobalFunc.RemoveAllChildren(root)
        j = 0
        maxCount = Model.Player.Player.MAX_VISIBLE_CARDS
        if len(cards) > 0:
            for c in cards:
                j += 1
                cardSpot = tk.Frame(root, name=self.CARD_SPOT+str(j), height=self.__cardHeight, width=self.__cardWidth)
                cardSpot.config(borderwidth=5, relief=RIDGE)
                cardSpot.pack(side=LEFT, pady=paddingY, padx=10)
                card = Card(c, self.__controller)
                card.Draw(cardSpot, self.__cardWidth, self.__cardHeight)
                cardSpot.bind("<Enter>", lambda e, area=cardSpot:self.MouseEnterArea(area))
                cardSpot.bind("<Leave>", lambda e, area=cardSpot:self.MouseLeaveArea(area))
                
                cardSpot.bind("<Button-1>", lambda e, card=c:self.__controller.SetAttackerDefender(card))
            
            
        for i in range(j,maxCount): #TODO: for c in hand:
            cardSpot = tk.Frame(root, name=self.CARD_SPOT+str(i), height=self.__cardHeight, width=self.__cardWidth)
            cardSpot.config(borderwidth=5, relief=RIDGE, background=Controller.Master.MasterController.BACKGROUND_COLOR)
            cardSpot.pack(side=LEFT, pady=paddingY, padx=10)
            cardSpot.bind("<Enter>", lambda e, area=cardSpot:self.MouseEnterArea(area))
            cardSpot.bind("<Leave>", lambda e, area=cardSpot:self.MouseLeaveArea(area))
            
    def RefreshBoard(self, playerOne, playerTwo):
        GlobalFunc.RemoveAllChildren(self.__cardAreaPlayerOne)
        GlobalFunc.RemoveAllChildren(self.__cardAreaPlayerTwo)
        GlobalFunc.RemoveAllChildren(self.__handCardArea)
        self.FillHandArea(playerOne)
        self.FillCardArea(self.__cardAreaPlayerOne, playerOne)
        self.FillCardArea(self.__cardAreaPlayerTwo, playerTwo)
        
    def AddInformation(self, informationText):
        GlobalFunc.RemoveAllChildren(self.__informationArea)
        information = tk.Frame(self.__informationArea, background=Controller.Master.MasterController.RED, borderwidth=5, relief=RIDGE)
        information.pack(fill=BOTH)
        label = tk.Label(information, text=informationText, background=Controller.Master.MasterController.RED)
        label.config(font=("Arial Black", 16, BOLD))
        label.pack()
        
    def MouseEnterArea(self, area):
        area.config(relief=SUNKEN)
        
    def MouseLeaveArea(self, area):
        area.config(relief=RIDGE)

    def RemoveFrame(self, frame):
        frame.destroy()
        
    def ResetInformation(self):
        GlobalFunc.RemoveAllChildren(self.__informationArea)
        self.__informationArea.config(background=Controller.Master.MasterController.BACKGROUND_COLOR)
        
    def GenerateTextPair(self, text, value, textArea, root):
        wrapper = tk.Frame(root, name=textArea, background=Controller.Master.MasterController.BACKGROUND_COLOR)
        wrapper.pack(fill=BOTH)
        
        label = tk.Label(wrapper, text=text)
        label.config(font=("Arial Black", 10), background=Controller.Master.MasterController.BACKGROUND_COLOR)
        label.pack(side=LEFT)
        
        text = tk.Label(wrapper, name=textArea+self.INPUT, text=value)
        text.config(font=("Arial Black", 10, tkFont.BOLD), background=Controller.Master.MasterController.BACKGROUND_COLOR)
        text.pack(side=LEFT)