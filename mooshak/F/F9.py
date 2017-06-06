__author__ = 'xyax'
import sys

xMax = yMax = 0
desenho = list()
for line in sys.stdin:
    retangulo = map(int, line.split())
    xMax = max(xMax, retangulo[2])
    yMax = max(yMax, retangulo[3])
    desenho.append(retangulo)

mapa = list()
for i in range(yMax+1):
    linha = list()
    for j in range(xMax+1):
        linha.append(' ')
    mapa.append(linha)

for d in desenho:
    for y in range(d[1], d[3]+1):
        for x in range(d[0], d[2]+1):
            mapa[y][x] = '#'

for m in mapa:
    print ''.join(m)