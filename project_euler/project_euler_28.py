#!/usr/bin/python

import euler

edge = 1001 # magic constant for edge number

def sum(edge):
    
    n = (edge + 1) / 2
    
    return int(\
        32 * euler.descendingFactorial(n, 3) / 6 + \
        20 * euler.descendingFactorial(n, 2) / 2 + \
        4 * n - \
        3) # 1 is alone, not on 4 corners.
    
    
print(sum(edge))