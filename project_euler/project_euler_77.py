#!/usr/bin/python

from euler import readPrimes

PRIMES = readPrimes( )
PRIMES.reverse()

ways  = {}

def countWays(money, coinIndex, coins):
    while money < coins[ coinIndex ] and coinIndex < len(coins) - 1:
        coinIndex += 1
    if money == 0:
        return 1
    if coinIndex == len(coins) - 1:
        if money % coins[ coinIndex ] == 0:
            return 1
        else:
            return 0
    p = (money, coinIndex)
    if p in ways:
        return ways[p]
    else:
        number = 0
        coin = coins[coinIndex]
        maxNumber = money // coin
        way = 0
        while number <= maxNumber:
            way += countWays(money - number * coin, coinIndex + 1, coins)
            number += 1
        ways[p] = way
        return way

assert( countWays( 10, 0, PRIMES ) == 5 )
assert( countWays( 1, 0, PRIMES ) == 0 )
assert( countWays( 71, 0, PRIMES ) == 5007 )

WAYS = 5000
i = 1
while countWays( i, 0, PRIMES ) <= WAYS:
    i += 1

assert( i == 71 )