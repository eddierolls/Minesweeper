# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:37:34 2021

@author: edwar
"""

import unittest
import player
import board
from unittest.mock import patch

class TestPlayer(unittest.TestCase):
    
    SAMPLEBOARD = (3,3,"XXOOXXXOX")
    
    def testHuman(self):
        bd = board.Board()
        bd.setupBoardFromTuple(self.SAMPLEBOARD)
        pyr = player.Player("human",bd)
        # Test placing a mine
        with patch('builtins.input', side_effect=["M","0 0"]):
            self.assertEqual(pyr.makeMove(),0)
            self.assertEqual(bd.mined,set([(0,0)]))
            self.assertEqual(len(bd.uncovered),0)
        
        with patch('builtins.input', side_effect=["G","2 0"]):
            self.assertEqual(pyr.makeMove(),0)
            self.assertEqual(len(bd.uncovered),1)
        

if __name__ == '__main__':
    unittest.main()