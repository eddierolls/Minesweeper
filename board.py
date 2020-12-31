# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:29:35 2020

@author: edwar

TODO:
    * Implement placing a mine (make sure that it hasn't been guessed)
    * Create a game object (probably seperate file)
"""
import random

class Board:
    """ The board on which the game is played"""
    
    def __init__(self,x=10,y=10,m=10,x0=0,y0=0):
        """ setup a board of size x by y, with m mines and initial guess (x0,y0) """
        if x<0 or y<0 or x*y<=m:
            raise ValueError("Invalid board dimensions")
        
        self.dim = (x,y)
        self.allSquares = set([(a,b) for a in range(x) for b in range(y)])
        self.uncovered = [] # Tuples (i,j,n) for the square (i,j) and the number of adjacent mines n
        self.mined = set()
        self.mines = self.__setupBoard__(m,x0,y0)
        self.finished = False
        self.lost = False
        self.guessSquare(x0,y0)
    
    def __setupBoard__(self,m,x0,y0):
        """ Sets up the board """
        x,y = self.dim
        mines = random.sample(range(x*y),m+1)
        mines = [(m//x,m%y) for m in sorted(mines)]
        if (x0,y0) in mines:
            mines.remove((x0,y0))
        else:
            mines = mines[:m]
        return set(mines)
    
    def __str__(self):
        """ Prints the state of the board """
        s = ["-"*(self.dim[0]+2)+"\n"]
        uncovered = [(a[0],a[1]) for a in self.uncovered]
        for j in range(self.dim[1]-1,-1,-1):
            s.append('|')
            for i in range(self.dim[0]):
                if (i,j) in self.mined:
                    s.append("X")
                elif (i,j) in uncovered and (i,j) in self.mines:
                    s.append("M")
                elif (i,j) in uncovered:
                    a = uncovered.index((i,j))
                    if self.uncovered[a][2]==0:
                        s.append(" ")
                    else:
                        s.append(str(self.uncovered[a][2]))
                else:
                    s.append("+")
            s.append("|\n")
        s.append("-"*(self.dim[0]+2)+"\n")
        if self.finished and self.lost:
            s.append("GAME LOST\n")
        elif self.finished:
            s.append("GAME WON")
        return "".join(s)
        
    def guessSquare(self,x0,y0):
        """ Make a guess """
        if (x0,y0) not in self.allSquares:
            return 1
        elif (x0,y0) in [(a[0],a[1]) for a in self.uncovered]:
            return 2 # Already guessed
        elif (x0,y0) in self.mined:
            return 3 # Already mined
        elif (x0,y0) in self.mines:
            self.finished = True
            self.lost = True
            self.uncovered.append((x0,y0,-1))
            return 4 # Game lost
        
        adjacent = [(x,y) for x in range(x0-1,x0+2) for y in range(y0-1,y0+2)
                    if (y>=0 and x>=0 and x<self.dim[1] and y<self.dim[1] and not (x==x0 and y==y0))]
        totalMines = len([a for a in adjacent if a in self.mines])
        self.uncovered.append((x0,y0,totalMines))
        if totalMines == 0:
            for a in adjacent:
                self.guessSquare(a[0],a[1])
        
        if len(self.uncovered) == self.dim[0]*self.dim[1]-len(self.mines):
            self.finished = True
            return 5 # Game won!
        
        return 0
        
        
    def placeMine(self,x0,y0):
        """ Place a mine on a square. If already mined then reverse. """
        if (x0,y0) not in self.allSquares:
            return 1
        if (x0,y0) in [(a[0],a[1]) for a in self.uncovered]:
            return 2 # Already guessed
        elif (x0,y0) in self.mined:
            self.mined.remove((x0,y0))
        else:
            self.mined.add((x0,y0))
        
        return 0 # Already mined
