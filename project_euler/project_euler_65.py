#!/usr/bin/python

acfs0 = [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14]

def termInContinuedFractionExpansionOfE(n): 
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        m = n % 3
        if m == 1:
            return 1
        elif m == 2:
            return 1
        else:
            return 2 * (n // 3)

acfs = []    
for n in range(0,len(acfs0)):
    acfs.append(termInContinuedFractionExpansionOfE(n + 1))

assert(acfs == acfs0)

def p(n):
    ps = [0,1]
    for i in range(1,n+1):
        p = termInContinuedFractionExpansionOfE(i) * ps[-1] + ps[-2]
        ps.append(p)
        ps.pop(0)
    return ps[-1]

# Main

assert(sum(map(int,str(p(100)))) == 272)
