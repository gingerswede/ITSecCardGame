'''
Created on 22 jul 2015

@author: Emil
'''

class OutOfMovesError(Exception):
    
    def __init__(self, args="OutOfMovesError"):
        self.message = args

class IncorrectAttackerError(Exception):
    
    def __init__(self, args="IncorrectAttackerError"):
        self.message = args