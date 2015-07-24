'''
Created on 22 jul 2015

@author: Emil
'''
import Model
import Tkinter as tk

class Card(object):
    
    __card = None
    __visible = False
    __root = None
    
    def __init__(self, card):
        if isinstance(card, Model.Card.Card):
            self.__card = card
            self.__visible = False
            
        else:
            raise TypeError
    
    @property
    def Visible(self):
        return self.__visible
    
    @Visible.setter 
    def Visible(self, visible):
        if type(visible) == bool:
            self.__visible = visible
        else:
            return TypeError
        
    @property
    def HealthPoints(self):
        return self.__card.HP
    
    @property
    def AttackPoints(self):
        return self.__card.AP
    
    @property
    def DefensePoints(self):
        return self.__card.DP
    
    def RenderCard(self):
        self.__root = tk.Frame(width=300, height=400)
        
        return self.__root