# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:13:32 2021

@author: edwar
"""

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


