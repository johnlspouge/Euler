#!/usr/bin/python

import euler

n = 20

primes0 = [2,3,5,7,11,13,17,19] 
primes = []
euler.appendToPrimes(n, primes)
assert primes == primes0

n = 30

euler.appendToPrimes(n, primes)
primes0 += [23,29]
assert primes == primes0

primeFactors0 = [2,5,23]
primeFactors = euler.primeFactors(230, primes)
assert primeFactors == primeFactors0

primeFactors0 = [2,2,3,3]
primeFactors = euler.primeFactors(36, primes)
assert primeFactors == primeFactors0

primePowerFactorization0 = {2:2,3:2}
primePowerFactorization = euler.primePowerFactorization(primeFactors)
assert primePowerFactorization0 == primePowerFactorization

assert(euler.descendingFactorial(5,2) == 20)
assert(euler.descendingFactorial(5,3) == 60)
assert(euler.ascendingFactorial(5,2) == 30)
assert(euler.ascendingFactorial(5,3) == 210)

assert(euler.descendingFactorial(5,-2) == 1/42)
assert(euler.descendingFactorial(5,-3) == 1/336)
assert(euler.ascendingFactorial(5,-2) == 1/12)
assert(euler.ascendingFactorial(5,-3) == 1/24)

assert(euler.factors(20,[]) == [1,2,4,5,10,20])

assert(euler.appendDigits(37465,[]) == [3,4,5,6,7])
assert(euler.appendDigitsUnsorted(37465,[]) == [3,7,4,6,5])

primes = euler.readPrimes()
assert( primes[ 0:20 ] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71] )
