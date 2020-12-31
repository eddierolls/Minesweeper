# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 18:22:38 2020

@author: edwar
TODO:
    * Create some kind of 'who's playing' option, where selecting a human plater plays what's currently in the init function
"""

import board

class Game:
    """ An instance of a game which sets up a board and controls I/O """
    
    def __init__(self):
        """ Currently where the game is played """
        self.board = self.setupBoard()
        print(self.board)
        while not self.board.finished:
            out = self.makeMove()
            if out == 1: break
            print(self.board)
            
            
    def setupBoard(self):
        x,y = parsePair("Select board dimensions as two numbers separated by a space:")
        m = int(input("How many mines should there be?\n"))
        x0,y0 = parsePair("What is your initial guess?")
        bd = board.Board(x,y,m,x0,y0)
        return bd
    
    def makeMove(self):
        valid = False
        while not valid:
            moveType = input("Would you like to place a mine (M), make a guess (G) or quit (Q)\n").upper()
            if moveType == "Q":
                return 1
            elif moveType not in ("G","M"):
                print("Sorry, that wasn't recognised, please try again.")
            else:
                valid = True
        moveName = "place the mine" if moveType=="M" else "make a guess"
        x0,y0 = parsePair("Where would you like to "+moveName)
        if moveType=="G":
            out = self.board.guessSquare(x0,y0)
        else:
            out = self.board.placeMine(x0,y0)
        
        if out==1:   print("That square is not on the board")
        elif out==2: print("That square has already been uncovered")
        elif out==3: print("That square has a mine on it, please select mine to undo this")
        elif out==4: print("Commiserations, you have lost!")
        elif out==5: print("Congratulations, you have won!")
            
# Static Methods
def parsePair(s=""):
    """ Parse a pair of numbers from input """
    valid = False
    while not valid:
        try:
            x,y = [int(a) for a in input(s+"\n").split(" ")]
            valid = True
        except ValueError:
            print("Please input two integer co-ordinates separated by a space")
    return x,y

if __name__ == "__main__":
    g = Game()