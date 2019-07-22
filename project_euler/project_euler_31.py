#!/usr/bin/python

ways  = {}

def countWays(money, coinIndex, coins):
    if money == 0 or coinIndex == len(coins) - 1:
        return 1
    p = (money, coinIndex)
    if p in ways:
        return ways[p]
    else:
        number = 0
        coin = COINS[coinIndex]
        maxNumber = money // coin
        way = 0
        while number <= maxNumber:
            way += countWays(money - number * coin, coinIndex + 1, coins)
            number += 1
        ways[p] = way
        return way

COINS = [200, 100, 50, 20, 10, 5, 2, 1] # coins circulating in England
MONEY = 200

print(countWays(MONEY, 0, COINS))
