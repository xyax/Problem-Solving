__author__ = 'xyax'
import sys
from collections import deque

x, y=map(int, raw_input().split())
matrix=list()
for line in sys.stdin:
    lline=list(line)
    if lline[-1]=='\n':
        lline.pop()
    matrix.append(lline)

colunas=max(map(len, matrix))
linhas= len(matrix)

mapa=list()
for i in range(linhas):
    l=list()
    for j in range(colunas):
        if j<len(matrix[i]):
            l.append(matrix[i][j])
        else:
            l.append(' ')
    mapa.append(l)

q=deque([(x, y)])
mapa[x][y]='#'
r=1
while(len(q)>0):
    v=q.popleft()
    adj=list()
    a, b= v[0]+1, v[1]
    if a < colunas:
        if not(mapa[a][b]=='*'):
            adj.append((a, b))
    a, b= v[0]-1, v[1]
    if a > 0:
        if not(mapa[a][b]=='*'):
            adj.append((a, b))
    a, b= v[0], v[1]+1
    if b <= linhas:
        if not(mapa[a][b]=='*'):
            adj.append((a, b))
    a, b= v[0], v[1]-1
    if b > 0:
        if not(mapa[a][b]=='*'):
            adj.append((a, b))
    for e in adj:
        xe, ye= e
        if mapa[xe][ye]==' ':
            q.append(e)
            mapa[xe][ye]='#'
            r+=1

print r