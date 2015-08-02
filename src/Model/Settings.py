'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
@copyright: 2015 Emil Carlsson
@license: This program is distributed under the terms of the GNU General Public License
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