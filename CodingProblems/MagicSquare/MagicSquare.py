#!/bin/python3

import math
import os
import random
import re
import sys
import collections
from Square import Square

# Complete the formingMagicSquare function below.
def formingMagicSquare(square):

    square.getterms()
    square.printinfo()

    numunused = len(square.unusedterms.keys())

    # Creates new dict of repeated locations mapped by location tuple
    # Allows to iterate through all repeated locations, and determine val by location.
    repeatvals = square.repeatterms.values()
    repeatkeys = square.repeatterms.keys()

    locationsaskeys = {}
    for oldkey in repeatkeys:
        for locationtuple in square.repeatterms[oldkey]:
            locationsaskeys[locationtuple] = oldkey


    mindiff = math.inf
    repeattarget = -1
    totalcost = 0
    # First order of business: Insert all unused
    # Determine smallest diff between available repeated terms and unused terms
    # Used locationsaskeys for easy iteration through all possible locations
    # Note: repeats only catalogue second instance or higher. Doesn't actually ensure magic square, just cost
    for unused in square.unusedterms.keys():
        for repeatlocation in locationsaskeys.keys():
            diff = abs(unused - locationsaskeys[repeatlocation])
            if diff < mindiff:
                mindiff = diff
                repeattarget = repeatlocation
            # Set entry for location that's getting changed to garbage value
            locationsaskeys[repeattarget] = math.inf
            totalcost += mindiff

    print("totalcost: " + str(totalcost))
    return (totalcost)


if __name__ == '__main__':
    s1 = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
    s2 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
    s3 = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

    S1 = Square(s1)
    S2 = Square(s2)
    S3 = Square(s3)

    # formingMagicSquare(S1)
    # formingMagicSquare(S2)
    formingMagicSquare(S3)

