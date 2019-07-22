#!/usr/bin/python

def newMatrix( m, n ):
    matrix = []
    for i in range( 0, m ):
        matrix.append( [0] * n )
    return matrix

def moveToNextCol( sumMatrix, matrix, j ):
    m = len( matrix )
    
    if j == 0:
        for i in range( 0, m ):
            sumMatrix[ i ][ 0 ] = matrix[ i ][ 0 ]
        return
        
    leftTo = [0] * m
    for i in range( 0, m ):
        leftTo[ i ] = sumMatrix[ i ][ j - 1 ] + matrix[ i ][ j ] 
    
    upTo = [0] * m
    for i in range( m - 1, -1, -1 ):
        if i == m - 1:
            upTo[ i ] = leftTo[ m - 1 ] 
        else:
            upTo[ i ] = min( upTo[ i + 1 ] + matrix[ i ][ j ], leftTo[ i ] )

    downTo = [0] * m
    for i in range( 0, m ):
        if i == 0:
            downTo[ i ] = leftTo[ 0 ]
        else:
            downTo[ i ] = min( downTo[ i - 1 ] + matrix[ i ][ j ], leftTo[ i ] )
        
    for i in range( 0, m ):
        sumMatrix[ i ][ j ] = min( leftTo[ i ], upTo[ i ], downTo[ i ] )

    return                

matrix = [
[ 131,673,234,103,18 ],
[ 201,96,342,965,150 ],
[ 630,803,746,422,111 ],
[ 537,699,497,121,956 ],
[ 805,732,524,37,331 ]
]

m = len( matrix )
n = len( matrix[ 0 ] )
sumMatrix = newMatrix( m, n )

for j in range( 0, n ):
    moveToNextCol( sumMatrix, matrix, j )

assert( min( [ sumMatrix[ i ][ -1 ] for i in range( 0, m ) ] ) == 994)

matrix = []
with open( 'Data/p082_matrix.txt', 'r' ) as myfile:
    line = myfile.readline()
    while line:
        matrix.append( [ int( field ) for field in line.split( ',' ) ] )
        line = myfile.readline()

m = len( matrix )
n = len( matrix[ 0 ] )
sumMatrix = newMatrix( m, n )

for j in range( 0, n ):
    moveToNextCol( sumMatrix, matrix, j )

assert( min( [ sumMatrix[ i ][ -1 ] for i in range( 0, m ) ] ) == 260324 )
