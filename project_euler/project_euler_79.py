#!/usr/bin/python

with open('Data/p079_keylog.txt', 'r') as content_file:
    content = content_file.read()

singles = []
pairs = []
passcodes = content.splitlines()
for p in passcodes:
    digits = [ ( p[ 0 ], p[ 1 ] ), ( p[ 0 ], p[ 2 ] ), ( p[ 1 ], p[ 2 ] ) ]
    pairs.extend( digits )
    singles.extend( list( p ) )
    
orders = list( set( pairs ) )
remains = list( set( singles ) )

lefts = []
while True:
    removes = [ i for i in remains if all( [ i != order[ 1 ] for order in orders ] ) ]
    if len( removes ) == 0:
        break
    lefts.extend( removes )
    for i in removes:
        remains.remove( i )
        removals = [ order for order in orders if i == order[ 0 ] ]
        for order in removals:
            orders.remove( order )

rights = []
while True:
    removes = [ i for i in remains if all( [ i != order[ 0 ] for order in orders ] ) ]
    if len( removes ) == 0:
        break
    rights.extend( removes )
    for i in removes:
        remains.remove( i )
        removals = [ order for order in orders if i == order[ 1 ] ]
        for order in removals:
            orders.remove( order )

linec = ''.join( lefts )
assert( linec == '73162890' )
assert( rights == [] )
assert( orders == [] )
assert( remains == [] )
