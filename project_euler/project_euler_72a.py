#!/usr/bin/python

import time

def F( n ):
    return n * (n - 1) // 2

assert( F( 8 ) == 28 )

n2fareyLength = dict({})

def fareyLength( n ):
    if n in n2fareyLength.keys():
        return n2fareyLength[ n ]
    length = F( n )
    for m in range( 2, n + 1 ):
        length -= fareyLength( n // m )
    n2fareyLength[ n ] = length
    return length

assert( fareyLength( 8 ) == 21  )
assert( fareyLength( 9 ) == 27  )

start = time.time()
assert( fareyLength( 10**6 ) == 303963552391 )
print( time.time() - start )
