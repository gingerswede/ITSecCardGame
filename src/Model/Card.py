'''
Created on 19 jul 2015

@author: Emil
'''

import re
class Card(object):
    
    __isAlive = None
    __hp = None
    __dp = None
    __ap = None
    __name = None
    __description = None
    __image = None
    
    def __init__(self, cardName=None, cardDescription=None, cardImage=None, cardAp=None, cardDp=None, cardHp=None):
        self.Name = cardName
        self.Description = cardDescription
        self.AP = cardAp
        self.DP = cardDp
        self.HP = cardHp
        self.Image = cardImage
        self.__isAlive = True
        
    @property
    def Name(self):
        if type(self.__name) == None:
            raise TypeError
        
        return self.__name
    
    @Name.setter
    def Name(self, cardName):
        if type(cardName) == str and len(cardName) > 3:
            self.__name = cardName
            
        else:
            raise TypeError
        
    @property
    def Image(self):
        if type(self.__image) == None:
            raise TypeError
        
        return self.__image
    
    @Image.setter
    def Image(self, cardImage):
        pattern = re.compile("^(https?:\/\/)([\da-z\.-]+)\.[a-z]*")
        if type(cardImage) == str and pattern.match(cardImage):
            self.__image = cardImage
            
        else:
            raise TypeError

    @property
    def AP(self):
        if type(self.__ap) == None:
            raise TypeError
        
        return self.__ap
    
    @AP.setter
    def AP(self, cardAp):
        if type(cardAp) == int and cardAp > 0:
            self.__ap = cardAp
        else:
            raise TypeError
    
    @property
    def DP(self):        
        if type(self.__dp) == None:
            raise TypeError
        return self.__dp
    
    @DP.setter
    def DP(self, cardDp):
        if type(cardDp) == int and cardDp > 0:
            self.__dp = cardDp
        else:
            raise TypeError
        
    @property
    def HP(self):
        return self.__hp
    
    @HP.setter
    def HP(self, cardHp):
        if type(cardHp) == int and cardHp > 0:
            self.__hp = cardHp
            if self.__hp < 1:
                self.__hp = 0
                self.__isAlive = False
        elif cardHp < 0:
            self.__hp = 0
            self.__isAlive = False
        else:
            raise TypeError
        
    @property
    def Description(self):
        if (self.__description) == None:
            raise TypeError
        
        return self.__description
    
    @Description.setter
    def Description(self, cardDescription):
        if type(cardDescription) == str and len(cardDescription) > 10:
            self.__description = cardDescription
            
        else:
            raise TypeError
        
    @property
    def IsAlive(self):
        if self.__hp <= 0:
            self.__isAlive = False
            return False
        else:
            return True
        
    def defend(self, other):
        if isinstance(other, Card):
            if self.DP < other.AP:
                self.HP = self.HP - (other.AP - self.DP)
                return other
            else:
                other.HP = other.HP - (self.DP - other.AP)        
                return self
        else:            
            raise TypeError