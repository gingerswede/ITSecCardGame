'''
Created on 28 jul 2015

@author: Emil
'''

class Settings(object):
    
    __music = None

    def __init__(self, *args, **kwargs):
        self.__music = False
        
    @property
    def Music(self):
        return self.__music
    
    @Music.setter
    def Music(self, value):
        if type(value) == bool:
            self.__music = value