#!/usr/bin/python

from euler import readPrimes

UPPER = 50 * 10 ** 6 # UPPER = 50  # 

primes = readPrimes( UPPER )

na = set({})

n2 = 0
while True:
    s2 = primes[ n2 ] ** 2 
    if s2 > UPPER:
        break
    n3 = 0
    while True:
        s3 = s2 + primes[ n3 ] ** 3
        if s3 > UPPER:
            break
        n4 = 0
        while True:
            s4 = s3 + primes[ n4 ] ** 4
            if s4 > UPPER:
                break
            else:
                na.add( s4 )
            n4 += 1
        n3 += 1
    n2 += 1
      
assert( len( na ) == 1097343 )      