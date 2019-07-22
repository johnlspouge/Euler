#!/usr/bin/python

from euler import appendDigits, appendToPrimes, isPrime

PRIMES = []
LOWER = 10**3
UPPER = 10**4
appendToPrimes(UPPER, PRIMES)

fourDigitPrimes = [p for p in PRIMES if LOWER <= p < UPPER]
assert(fourDigitPrimes[0] == 1009)
assert(isPrime(1009, PRIMES))
assert(fourDigitPrimes[-1] == 9973)
assert(isPrime(9973, PRIMES))

for p1 in fourDigitPrimes:
    digits1 = []
    appendDigits(p1, digits1)
    for p0 in fourDigitPrimes:
        if p1 <= p0:
            break
        assert(p0 < p1)
        digits0 = []
        appendDigits(p0, digits0)
        if digits0 != digits1:
            continue
        else:
            p2 = p1 + (p1 - p0) # next in the arithmetic series
            assert(p1 < p2)
            if p2 not in fourDigitPrimes:
                continue
            digits2 = []
            appendDigits(p2, digits2)
            if digits2 != digits1:
                continue
            else:
                print(str(p0) + str(p1) + str(p2))
