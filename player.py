# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:01:32 2021

@author: edwar
"""

import minefieldUtility as util
import random

class Player:
    
    def __init__(self,playerType,bd):
        if playerType not in ["human" "random"]:
            TypeError("playerType not recognised")
        self.playerType = playerType
        self.board = bd
    
    def makeMove(self):
        fn = getattr(self,self.playerType+"Move")
        out = fn()
        return out
        
    def humanMove(self):
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
        x0,y0 = util.parsePair("Where would you like to "+moveName)
        if moveType=="G":
            out = self.board.guessSquare(x0,y0)
        else:
            out = self.board.placeMine(x0,y0)
        
        if out==1:   print("That square is not on the board")
        elif out==2: print("That square has already been uncovered")
        elif out==3: print("That square has a mine on it, please select mine to undo this")
        elif out==4: print("Commiserations, you have lost!")
        elif out==5: print("Congratulations, you have won!")
        return out
    
    def randomMove(self):
        validMoves = self.board.findValidModes()
        move = random.choice(tuple(validMoves))
        out = self.board.guessSquare(move[0],move[1])
        return out