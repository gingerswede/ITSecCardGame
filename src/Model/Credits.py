'''
Created on 28 jul 2015

@author: Emil
'''

class Credits(object):
    __music = None
    __soundEffects = None
    __source = None
    __images = None

    def __init__(self, *args, **kwargs):
        self.__music = ["Matti Paalanen (https://www.jamendo.com/en/list/a145266/inspirational)"]
        self.__soundEffects = ["pepv (https://www.freesound.org/people/pepv/)", 
                               "oceanictrancer (https://www.freesound.org/people/oceanictrancer/)", 
                               "julesibulesi (https://www.freesound.org/people/julesibulesi/)", 
                               "Streety (https://www.freesound.org/people/Streety/)", 
                               "deraj (https://www.freesound.org/people/deraj/)", 
                               "f4ngy (https://www.freesound.org/people/f4ngy/)"]
        self.__source = ["Emil Carlsson (https://github.com/gingerswede)"]
        self.__images = []
        
    @property
    def Music(self):
        return self.__music
    
    @property
    def Source(self):
        return self.__source
    
    @property
    def SoundEffects(self):
        return self.__soundEffects
    
    @property
    def Images(self):
        return self.__images
        