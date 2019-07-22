#!/usr/bin/python

import math

with open('Data/p099_base_exp.txt', 'r') as content_file:
    content = content_file.read()

pairs = content.splitlines()
maximum = -1
n = 0
for i in range( 0, len( pairs ) ):
    bs = pairs[ i ].split( ',' )
    log = float( bs[ 1 ] ) * math.log10( float( bs[ 0 ] ) )
    if maximum < log:
        n = i
        maximum = log
        
print( n + 1 )
