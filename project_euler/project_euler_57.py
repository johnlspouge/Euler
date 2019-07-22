#!/usr/bin/python

# http://mathworld.wolfram.com/PellEquation.html

def continuedFractionConvergentsSqrt2(): 
    oneDigitMore = 0
    powerOfTenInDenominator = 1
    ps = [0,1,1]
    qs = [1,0,1]
    for i in range(0,1000):
        q = 2 * qs[-1] + qs[-2]
        qs.append(q)
        qs.pop(0)
        if 10 <= q // powerOfTenInDenominator:
            powerOfTenInDenominator *= 10
        p = 2 * ps[-1] + ps[-2]
        ps.append(p)
        ps.pop(0)
        if 10 <= p // powerOfTenInDenominator:
            oneDigitMore += 1
        
    return oneDigitMore

# Main

assert(continuedFractionConvergentsSqrt2() == 153)
