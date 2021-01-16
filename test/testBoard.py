# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 13:14:16 2021

@author: edwar
"""

import unittest
import board

class TestBoard(unittest.TestCase):
    
    SAMPLEBOARD = (3,3,"XXOOXXXOX")

    def testSimpleInitialise(self):
        bd = board.Board((5,5,20,2,2)) # create a sample board
        self.assertEqual(bd.dim,(5,5))
        self.assertFalse(bd.lost or bd.finished)
        self.assertEqual(len(bd.mined),0)
        self.assertEqual(len(bd.allSquares-bd.mines),5)
        
    def testAutomaticWinInitialise(self):
        bd = board.Board((5,5,24,2,2))
        self.assertTrue(bd.finished)
        self.assertFalse(bd.lost)
        self.assertNotIn((2,2),bd.mines)
        self.assertEqual(len(bd.uncovered),1)
    
    def testSetupBoardFromTuple(self):
        bd = board.Board()
        bd.setupBoardFromTuple(self.SAMPLEBOARD)
        self.assertEqual(bd.dim,(3,3))
        self.assertEqual(len(bd.mines),6)
        self.assertEqual(bd.mines,set([(0,0),(1,0),(1,1),(2,1),(0,2),(2,2)]))
    
    def testGuessSquare(self):
        bd = board.Board()
        bd.setupBoardFromTuple(self.SAMPLEBOARD)
        self.assertEqual(bd.guessSquare(3,3),1) # Off the board
        self.assertEqual(bd.guessSquare(2,0),0) # Legal move
        self.assertEqual(bd.guessSquare(2,0),2) # Already uncovered
        self.assertEqual(bd.guessSquare(0,1),0) # Legal move
        self.assertEqual(bd.guessSquare(1,2),5) # Win
        
        bd = board.Board()
        bd.setupBoardFromTuple(self.SAMPLEBOARD)
        self.assertEqual(bd.guessSquare(0,0),4) # Loss
        
    
    def testPlaceMine(self):
        bd = board.Board()
        bd.setupBoardFromTuple(self.SAMPLEBOARD)
        bd.placeMine(0,0)
        self.assertEqual(bd.guessSquare(0,0),3) # Mine already there
        bd.placeMine(0,0)
        self.assertEqual(bd.guessSquare(0,0),4) # Loss
    
    def testFindValidModes(self):
        bd = board.Board((2,2,1,0,0))
        validMoves = bd.findValidModes()
        self.assertEqual(validMoves,set([(0,1),(1,1),(1,0)]))

if __name__ == '__main__':
    unittest.main()