__author__ = 'xyax'
import sys
from collections import deque

# le ponto interior
x, y = map(int, raw_input().split())
# check
#constroi mapa
drawIn = list()
for line in sys.stdin:
    lline = list(line)
    if lline[-1] == '\n':
        lline.pop()
    drawIn.append(lline)

linhas = len(drawIn)
colunas = max(map(len, drawIn))
#check

#completa mapa com espacos
for i in range(linhas):
    for j in range(colunas):
        if j >= len(drawIn[i]):
            drawIn[i].append(' ')
#check
#constroi grafo
graph = dict()
for i in range(linhas):
    for j in range(colunas):
        p = (j, i)
        graph[p] = list()
        if j + 1 < colunas:
            graph[p].append((j + 1, i))
        if j - 1 >= 0:
            graph[p].append((j - 1, i))
        if i + 1 < linhas:
            graph[p].append((j, i + 1))
        if i - 1 >= 0:
            graph[p].append((j, i - 1))
#check
#percorre vertices acessiveis a partir de (x, y) e marca-los como visitados: '#'
q = deque([(x, y)])
drawIn[y][x] = '#'
while len(q) > 0:
    v = q.popleft()
    for e in graph[v]:
        xe, ye = e
        if drawIn[ye][xe] == ' ':
            q.append(e)
            drawIn[ye][xe] = '#'
#check
#conta visitados
r = reduce(lambda a, b: a + b, map(lambda c: c.count('#'), drawIn))

print r
