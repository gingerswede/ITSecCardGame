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

class MaxHandSize(Exception):
    
    def __init__(self, args="MaxHandsize"):
        self.message = args
        
class CardNotInHand(Exception):
    
    def __init__(self, args="CardNotInHand"):
        self.message = args
        
class MaxVisibleHandSize(Exception):
    
    def __init__(self, args="MaxVisibleHandSize"):
        self.message = args
        