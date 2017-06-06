__author__ = 'xyax'
#!/usr/bin/python
import sys

def printMatrix(matrix):
    for m in matrix:
        print ''.join(m)

xMin= yMin = sys.maxint
xMax= yMax = -1
retangulos= list()
for line in sys.stdin:
    lLine= line.split()
    retangulos.append(lLine)
    xMin= min(xMin, int(lLine[0]))
    xMax= max(xMax, int(lLine[2]))
    yMin= min(yMin, int(lLine[1]))
    yMax= max(yMax, int(lLine[3]))

matrix= list()

for y in range(yMin, yMax+1):
    l= list()
    for x in range(xMin, xMax+1):
        l.append(' ')
    matrix.append(l)

for r in retangulos:
    for y in range(int(r[1]), int(r[3])+1):
        for x in range(int(r[0]), int(r[2])+1):
            matrix[y][x]= '#'

printMatrix(matrix)