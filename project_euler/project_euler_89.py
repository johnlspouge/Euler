#!/usr/bin/python

import re

LETTER2NUMERAL = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
}

assert( LETTER2NUMERAL[ 'L' ] == 50 )

def toInteger( romanc ):
    romanc = romanc[::-1]
    numeral0 = 0
    n = 0
    while len( romanc ) != 0:
        numeral = LETTER2NUMERAL[ romanc[ 0 ] ]
        romanc = romanc[ 1: ]
        if numeral < numeral0:
            n -= numeral
        else:
            n += numeral
        numeral0 = numeral
    return n

assert( toInteger( 'IIIIIIIIIIIIIIII' ) == 16 )
assert( toInteger( 'VIIIIIIIIIII' ) == 16 )
assert( toInteger( 'VVIIIIII' ) == 16 )
assert( toInteger( 'XIIIIII' ) == 16 )
assert( toInteger( 'VVVI' ) == 16 )
assert( toInteger( 'XVI' ) == 16 )
assert( toInteger( 'XIV' ) == 14 )

def toRoman( n ):
    romanc = '' 
    while n >= 1000:
        romanc += 'M'
        n -= 1000
    if n >= 900:
        romanc += 'CM'
        n -= 900
    if n >= 500:
        romanc += 'D'
        n -= 500
    if n >= 400:
        romanc += 'CD'
        n -= 400
    while n >= 100:
        romanc += 'C'
        n -= 100
    if n >= 90:
        romanc += 'XC'
        n -= 90
    if n >= 50:
        romanc += 'L'
        n -= 50
    if n >= 40:
        romanc += 'XL'
        n -= 40
    while n >= 10:
        romanc += 'X'
        n -= 10
    if n >= 9:
        romanc += 'IX'
        n -= 9
    if n >= 5:
        romanc += 'V'
        n -= 5
    if n >= 4:
        romanc += 'IV'
        n -= 4
    while n >= 1:
        romanc += 'I'
        n -= 1
    assert( n == 0 )
    return romanc

assert( toRoman( 16 ) == 'XVI' )
assert( toRoman( 14 ) == 'XIV' )
assert( toInteger( 'MMMMDCLXXII' ) == 4672 )
assert( toRoman( 4672 ) == 'MMMMDCLXXII' )

saved = 0
with open( 'Data/p089_roman.txt', 'r' ) as myfile:
    line = myfile.readline()
    while line:
        pattern = re.compile(r'\s+')
        line = re.sub(pattern, '', line)
#        print( line )
        saved += len( line )
        n = toInteger( line )
        romanc = toRoman( n )
        saved -= len( romanc )
        line = myfile.readline()

print( saved ) 
