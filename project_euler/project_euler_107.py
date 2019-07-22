#!/usr/bin/python

from math import inf
import re

weight_css = """\
  	A	B	C	D	E	F	G
A	-	16	12	21	-	-	-
B	16	-	-	17	20	-	-
C	12	-	-	28	-	31	-
D	21	17	28	-	18	19	23
E	-	20	-	18	-	-	11
F	-	-	31	19	-	-	27
G	-	-	-	23	11	27	-"""

def toNumber( w_c ):
    if w_c == '-':
        w_i = inf
    else:
        w_i = int( w_c )
    return w_i

def toNetwork( weight_css ):
    weight_iss = []
    s_cs = weight_css.split( "\n" )
    s_cs.pop( 0 )
    for s_c in s_cs:
        field_cs = re.split( "\s+", s_c )
        field_cs.pop( 0 )
        w_is = []
        for w_c in field_cs:
            w_is.append( toNumber( w_c ) )
        weight_iss.append( w_is )
    return weight_iss

def readNetwork():
    weight_iss = []
    with open( 'Data/p107_network.txt', 'r' ) as myfile:
        lines = myfile.read().splitlines()
        while len( lines ) != 0:
            line = lines.pop( 0 )
            w_cs = line.split( ',' )
            w_is = []
            for w_c in w_cs:
                if w_c == '-':
                    w_i = inf
                else:
                    w_i = int( w_c )
                w_is.append( w_i )
            weight_iss.append( w_is )
    return weight_iss
    
def isConnected( weight_iss ):
    notVisited_is = set( range( 0, len( weight_iss ) ) )
    visited_is = [ 0 ] # Starts probing at 0.
    notVisited_is.remove( 0 )
    while len( visited_is ) != 0:
        v = visited_is.pop( 0 )
        for i in range( 0, len( weight_iss ) ):
            if weight_iss[ v ][ i ] != inf and i in notVisited_is:
                visited_is.append( i )
                notVisited_is.remove( i )
    return len( notVisited_is ) == 0

assert( isConnected( toNetwork( weight_css ) ) )

def sortedEdges( weight_iss ):
    edges = []
    for i in range( 0, len( weight_iss ) ):
        for j in range( i, len( weight_iss[ 0 ] ) ):
            if weight_iss[ i ][ j ] != inf:
                edges.append( ( weight_iss[ i ][ j ], i, j ) )
    edges.sort( reverse = True )
    return edges
    
#print( toNetwork( weight_css ) )
#print( sortedEdges( toNetwork( weight_css ) ) )

def greedyRemoveSave( weight_iss ):
    treeEdgeCount = len( weight_iss ) - 1
    edges = sortedEdges( weight_iss )
    save = 0
    for edge in edges:
        if len( edges ) == treeEdgeCount:
            break
        i, j = edge[ 1 ], edge[ 2 ]
        weight = weight_iss[ i ][ j ]
        weight_iss[ i ][ j ] = inf # Tries removing the edge [i, j]
        weight_iss[ j ][ i ] = inf # Tries removing the edge [i, j]
        if not isConnected( weight_iss ):
            weight_iss[ i ][ j ] = weight
            weight_iss[ j ][ i ] = weight
        else:
            save += weight
    #print( weight_iss )
    return save
                
assert( greedyRemoveSave( toNetwork( weight_css ) ) == 150 )           
assert( greedyRemoveSave( readNetwork() ) == 259679 )            
    
    
    