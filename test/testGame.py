# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 13:30:47 2021

@author: edwar
"""

import unittest
import game
from unittest.mock import patch

class TestGame(unittest.TestCase):
    
    def testInit(self):
        gm = game.Game(params=(3,3,7,1,1),printToScreen=False) # create a 3x3 board with 8 mines to finish immediately
        bd = gm.board
        self.assertEqual(bd.dim,(3,3))
        self.assertFalse(bd.lost)
        self.assertFalse(bd.finished)
        self.assertEqual(bd.uncovered[0],(1,1,7))
        self.assertEqual(len(bd.mines),7)
    
    def testSetupBoard(self):
        with patch('builtins.input', side_effect=["3 3","8","1 1"]):
            gm = game.Game(printToScreen=False)
            bd = gm.board
            self.assertEqual(bd.dim,(3,3))
            self.assertTrue(bd.finished)
            self.assertFalse(bd.lost)
            self.assertEqual(bd.uncovered[0],(1,1,8))
            self.assertEqual(len(bd.mines),8)
            
    def testPlayGame(self):
        for _ in range(20):
            gm = game.Game(params=(3,3,7,1,1),printToScreen=False) # create a 3x3 board with 8 mines to finish immediately
            with patch('builtins.input', side_effect=["G","0 0"]):
                self.assertIn(gm.playGame(),[0,1])
        

if __name__ == '__main__':
    unittest.main()