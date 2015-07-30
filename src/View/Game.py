'''
IDE: Eclipse (PyDev)
Python version: 2.7
Operating system: Windows 8.1

@author: Emil Carlsson
@copyright: 2015 Emil Carlsson
@license: This program is distributed under the terms of the GNU General Public License
'''
from View import GlobalFunc
from View.Board import Board

class GameView(object):
    
    __root = None
    __controller = None
    
    __boardView = None
    
    def __init__(self, root, gameController, *args, **kwargs):
        self.__root = root
        self.__controller = gameController
        
    def StartNewGame(self, player=None, opponent=None):
        GlobalFunc.RemoveAllChildren(self.__root)
        self.__boardView = Board(self.__root, self.__controller, player, opponent)
        
    def OutOfMoves(self):
        self.__boardView.AddInformation("You are out of moves.\nPlease finnish your turn.")
        
    def ResetInformation(self):
        self.__boardView.ResetInformation()
        
    def MaxHandSize(self):
        self.__boardView.AddInformation("Maximum hand size reached.\nPlease play a card if possible.")
        
    def MaxVisibleHandSize(self):
        self.__boardView.AddInformation("Maximum amount of visible cards reached.")
        
    def RefreshBoard(self, playerOne, playerTwo):
        self.__boardView.RefreshBoard(playerOne, playerTwo)            
        
    def RemoveFrame(self, frame):
        frame.destroy()
        
    def PlayerLost(self):
        self.__boardView.AddInformation("You lost!\nGame Over!")
        
    def PlayerWon(self):
        self.__boardView.AddInformation("You won!\nGame Over!")
        
    def OutOfCards(self):
        self.__boardView.AddInformation("You are out of cards in your deck.")
    
    def CardNotInHand(self):
        self.__boardView.AddInformation("Card not on your hand.")
    
    #TODO: Does not show
    def WaitingForOpponent(self):
        self.__boardView.AddInformation("Waiting for opponent...")
        
    def AppendMessage(self, message):
        self.__boardView.AppendInformation(message)