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

class Game:
    """ An instance of a game which sets up a board and controls I/O """
    
    def __init__(self,params=None,user="human"):
        """ Currently where the game is played """
        self.initialiseBoard(params)
        user = player.Player(user,self.board)
        while not self.board.finished:
            out = user.makeMove()
            if out == 1: break
            print(self.board)
    
    def initialiseBoard(self,params):
        if params==None: # Human game
            self.board = self.setupBoard()
            print(self.board)
        else: # AI
            x,y,m,x0,y0 = params
            self.board = board.Board(x,y,m,x0,y0)
    
    def setupBoard(self):
        x,y = util.parsePair("Select board dimensions as two numbers separated by a space:")
        m = int(input("How many mines should there be?\n"))
        x0,y0 = util.parsePair("What is your initial guess?")
        bd = board.Board(x,y,m,x0,y0)
        return bd
    
if __name__ == "__main__":
    g = Game()