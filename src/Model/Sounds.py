'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
@copyright: 2015 Emil Carlsson
@license: This program is distributed under the terms of the GNU General Public License
'''

import os

class Sounds(object):
    
    @property
    def CardFlip(self):
        path = os.path.join(os.path.abspath(os.getcwd()), "..", "sound", "card_flip.wav")
        return path
    
    @property
    def CardPlace(self):
        path = os.path.join(os.path.abspath(os.getcwd()), "..", "sound", "card_flip_reverse.wav")
        return path
    
    @property
    def Shuffle(self):
        path = os.path.join(os.path.abspath(os.getcwd()), "..", "sound", "shuffle.wav")
        return path
    
    @property
    def MenuMusic(self):
        path = os.path.join(os.path.abspath(os.getcwd()), "..", "sound", "menu.wav")
        return path
    
    @property
    def GamePlayMusic(self):
        path = os.path.join(os.path.abspath(os.getcwd()), "..", "sound", "gameplay.wav")
        return path
    
    @property
    def Click(self):
        path = os.path.join(os.path.abspath(os.getcwd()), "..", "sound", "click.wav")
        return path
    
    @property
    def Shot(self):
        path = os.path.join(os.path.abspath(os.getcwd()), "..", "sound", "shot.wav")
        return path
    
    @property
    def EndCredit(self):
        path = os.path.join(os.path.abspath(os.getcwd()), "..", "sound", "end_credit.wav")
        return path
        
        