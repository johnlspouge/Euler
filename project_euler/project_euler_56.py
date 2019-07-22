#!/usr/bin/python

UPPER = 100

def digitSum( n ):
    return sum( list( map( int, list( str( n ) ) ) ) )

maximum = 0
for a in range( 1, UPPER ):
    for b in range( 1, UPPER ):
        maximand = digitSum( a**b )
        if maximum < maximand:
            maximum = maximand
            
print( maximum )