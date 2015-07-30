'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
@copyright: 2015 Emil Carlsson
@license: This program is distributed under the terms of the GNU General Public License
'''
import Model

import Tkinter as tk
from Tkconstants import LEFT

from PIL import ImageTk
from tkFont import BOLD


class Card(object):
    
    __healthPoints = None
    __attackPoints = None
    __defensePoints = None
    __image = None
    __description = None
    __name = None
    
    __root = None
    
    __image = None
    
    def __init__(self, card, controller):
        if isinstance(card, Model.Card.Card):
            self.__controller = controller
            self.__card = card
            self.__attackPoints = card.AP
            self.__defensePoints = card.DP
            self.__healthPoints = card.HP
            self.__description = card.Description
            self.__image = card.Image
            self.__name = card.Name
            
        else:
            raise TypeError
    
    def Draw(self, root, height, width):
        base = tk.Frame(root, height=height, width=width)
        base.bind("<Button-1>", lambda e, card=self.__card:self.__controller.PlayCard(card))
        base.pack(side=LEFT, padx=5)
        
        title = tk.Label(base, text=self.__name)
        title.config(font=("Arial", 12, BOLD))
        title.bind("<Button-1>", lambda e, card=self.__card:self.__controller.PlayCard(card))
        title.pack()
                
        img = ImageTk.PhotoImage(self.__image)
        self.__img = img
        imgLabel = tk.Label(base, image=img)
        imgLabel.bind("<Button-1>", lambda e, card=self.__card:self.__controller.PlayCard(card))
        imgLabel.pack()
        
        cardInformationText = "AP: %d | DP: %d | HP: %d" % (self.__attackPoints, self.__defensePoints, self.__healthPoints)
        cardInformationFrame = tk.Label(base, text=cardInformationText, width=width)
        cardInformationFrame.config(font=("Arial", 10))
        cardInformationFrame.bind("<Button-1>", lambda e, card=self.__card:self.__controller.PlayCard(card))
        cardInformationFrame.pack()
        
        
        description = tk.Label(base, text=self.__description, wraplength=width-15, width=width)
        description.config(font=("Arial", 8))
        description.bind("<Button-1>", lambda e, card=self.__card:self.__controller.PlayCard(card))
        description.pack()