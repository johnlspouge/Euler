#!/usr/bin/python

def sums( line, sums0 ):
    ns = [ int( field ) for field in line.split( ',' ) ]
    assert( len( sums0 ) == 0 or len( ns ) == len( sums0 ) )
    sums = []
    if len( sums0 ) == 0:
        sums.append( ns[ 0 ])
        for i in range( 1 , len( ns ) ):
            sums.append( ns[ i ] + sums[ i - 1 ] )
        assert( len( sums ) == len( ns ) )
    else:
        sums.append( sums0[ 0 ] + ns[ 0 ])
        for i in range( 1 , len( ns ) ):
            s = min( sums0[ i ], sums[ i - 1 ])
            sums.append( ns[ i ] + s )
        assert( len( sums ) == len( ns ) )
    return sums

nss = [
[ 131,673,234,103,18 ],
[ 201,96,342,965,150 ],
[ 630,803,746,422,111 ],
[ 537,699,497,121,956 ],
[ 805,732,524,37,331 ]
]

sums0 = []

for ns in nss:
    line = ','.join( map( str, ns ) )
    sums0 = sums( line, sums0 )
assert( sums0[ -1 ] == 2427)

sums0 = []
with open( 'Data/p081_matrix.txt', 'r' ) as myfile:
    line = myfile.readline()
    line.strip()
    while line:
        sums0 = sums( line, sums0 )
        line = myfile.readline()
assert( sums0[ -1 ] == 427337)
