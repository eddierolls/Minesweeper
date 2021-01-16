# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 18:22:38 2020

@author: edwar
TODO:
    * Create some kind of 'who's playing' option, where selecting a human plater plays what's currently in the init function
"""

import board
import player
import minefieldUtility as util
import sys

class Game:
    """ An instance of a game which sets up a board and controls I/O """
    
    def __init__(self,params=None,user="human",printToScreen=True):
        """ Currently where the game is played """
        self.printToScreen = printToScreen
        self.initialiseBoard(params)
        self.player = player.Player(user,self.board)
    
    def playGame(self):
        while not self.board.finished:
            out = self.player.makeMove()
            if out == -1: return -1
            if self.printToScreen:
                printMessage(out)
                print(self.board)
        return 1-self.board.lost
    
    def initialiseBoard(self,params):
        if params==None: # Human game, need to get dimensions from the player
            self.board = self.setupBoard()
            if self.printToScreen: print(self.board)
        else: # AI, board dimensions defined
            self.board = board.Board(params)
    
    def setupBoard(self):
        x,y = util.parsePair("Select board dimensions as two numbers separated by a space:")
        m = int(input("How many mines should there be?\n"))
        x0,y0 = util.parsePair("What is your initial guess?")
        bd = board.Board((x,y,m,x0,y0))
        return bd

    
        
def printMessage(out):
    if out==1:   print("That square is not on the board")
    elif out==2: print("That square has already been uncovered")
    elif out==3: print("That square has a mine on it, please select mine to undo this")
    elif out==4: print("Commiserations, you have lost!")
    elif out==5: print("Congratulations, you have won!")
    
if __name__ == "__main__":
    if len(sys.argv)==1:
        g = Game()
    elif len(sys.argv)==2:
        g = Game(user=sys.argv[1])
    else:
        IOError("Expected a maximum of one command line argument")
    g.playGame()
