'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
'''

class Settings(object):
    
    __music = None

    def __init__(self, *args, **kwargs):
        self.__music = True
        
    @property
    def Music(self):
        return self.__music
    
    @Music.setter
    def Music(self, value):
        if type(value) == bool:
            self.__music = value