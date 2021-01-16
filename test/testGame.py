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
        gm = game.Game((3,3,8,1,1)) # create a 3x3 board with 8 mines to finish immediately
        bd = gm.board
        self.assertEqual(bd.dim,(3,3))
        self.assertFalse(bd.lost or not bd.finished)
        self.assertEqual(bd.uncovered[0],(1,1,8))
        self.assertEqual(len(bd.mines),8)
    
    def testSetupBoard(self):
        with patch('builtins.input', side_effect=["3 3","8","1 1"]):
            gm = game.Game()
            bd = gm.board
            self.assertEqual(bd.dim,(3,3))
            self.assertFalse(bd.lost or not bd.finished)
            self.assertEqual(bd.uncovered[0],(1,1,8))
            self.assertEqual(len(bd.mines),8)
        

if __name__ == '__main__':
    unittest.main()