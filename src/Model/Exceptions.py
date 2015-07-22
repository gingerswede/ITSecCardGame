'''
Created on 22 jul 2015

@author: Emil
'''

class OutOfMovesError(Exception):
    
    def __init__(self, args):
        self.message = args
        