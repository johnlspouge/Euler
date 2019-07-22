#!/usr/bin/python

def sums( s, sums0 ):
    ns = [ int( field ) for field in s.split() ]
    assert( len( ns ) == len( sums0 ) + 1 )
    if len( ns ) == 1:
        sums = [ ns[ 0 ] ]
    else:
        sums = []
        for i in range( 0 , len( ns ) ):
            if i == 0:
                maximum = ns[ i ] + sums0[ i ]
            elif i == len( ns ) - 1:
                maximum = ns[ i ] + sums0[ i - 1 ]
            else:
                maximum = ns[ i ] + max( sums0[ i - 1 ], sums0[ i ] ) 
            sums.append( maximum )
    return sums

ss = sums( '3', [] )
assert( ss == [3] )
ss = sums( '7 4', ss )
assert( ss == [10, 7] )
ss = sums( '2 4 6', ss )
assert( ss == [12, 14, 13] )
ss = sums( '8 5 9 3', ss )
assert( ss == [20, 19, 23, 16] )
    
ss = []
with open( 'Data/p067_triangle.txt', 'r' ) as myfile:
    s = myfile.readline()
    while s:
        ss = sums( s, ss )
        s = myfile.readline()

print( max( ss ) )