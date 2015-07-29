'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
@copyright: 2015 Emil Carlsson
@license: This program is distributed under the terms of the GNU General Public License
'''

class Credits(object):
    __music = None
    __soundEffects = None
    __source = None
    __images = None
    __license = None

    def __init__(self, *args, **kwargs):
        self.__music = ["Matti Paalanen (https://www.jamendo.com/en/list/a145266/inspirational)"]
        self.__soundEffects = ["pepv (https://www.freesound.org/people/pepv/)", 
                               "oceanictrancer (https://www.freesound.org/people/oceanictrancer/)", 
                               "julesibulesi (https://www.freesound.org/people/julesibulesi/)", 
                               "Streety (https://www.freesound.org/people/Streety/)", 
                               "deraj (https://www.freesound.org/people/deraj/)", 
                               "f4ngy (https://www.freesound.org/people/f4ngy/)"]
        self.__source = ["Emil Carlsson (https://github.com/gingerswede)"]
        self.__images = ["Wikipedia (http://www.wikipedia.org/)",
                         "Little Visuals (http://littlevisuals.co/)",
                         "Pixabay (https://pixabay.com/)",
                         "Ryan Somma (https://www.flickr.com/photos/ideonexus/)",
                         "Edwind Richzendy Contreras Soto (https://www.flickr.com/photos/35484468@N07/)"]
        self.__license = "This program is distributed under the terms of the GNU General Public License\nCopyright 2015 Emil Carlsson"
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
    
    @property
    def License(self):
        return self.__license
        