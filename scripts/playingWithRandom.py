# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 17:54:05 2021

@author: edwar
"""

import game
import random

wins = 0
for ii in range(1000):
    firstMove = random.choices(range(10),k=2)
    gm = game.Game(params=(10,10,10,firstMove[0],firstMove[1]),user="random",printToScreen=False)
    wins += gm.playGame()
    if ii%10==0:
        print(ii)
print(wins)