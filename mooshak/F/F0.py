__author__ = 'xyax'
#!/usr/bin/python
import sys

xMax= yMax = -1
retangulos= list()

for line in sys.stdin:
    lLine= line.split()
    retangulos.append(lLine)
    xMax= max(xMax, int(lLine[2]))
    yMax= max(yMax, int(lLine[3]))

matrix= [[' ' for i in range(xMax+1)] for i in range(yMax+1)]

for r in retangulos:
    for y in range(int(r[1]), int(r[3])+1):
        for x in range(int(r[0]), int(r[2])+1):
            matrix[y][x]= '#'

for m in matrix:
    print ''.join(m)