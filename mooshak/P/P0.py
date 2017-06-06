__author__ = 'xyax'
import sys

def Dijkstra(G1, source):
    #inf funciona como "infinito"
    inf = sys.maxint
    dist = dict()
    q = list()
    for v in G1.keys():
        dist[v] = inf
        q.append(v)
    dist[source] = 0
    while len(q) > 0:
        m = inf
        vert = str()
        for e in q:
            if m > dist[e]:
                m= dist[e]
                vert = e
        u = q.pop(q.index(vert))
        #vamos percorrer todos os vertices adjacentes de u
        for v in G1[u]:
            alt = dist[u] +1
            if alt < dist[v]:
                dist[v] = alt
    return dist

N = int(raw_input())
draw = list()
G = dict()
for line in sys.stdin:
    lline = list(line)
    if lline[-1] == '\n':
        lline.pop()
    draw.append(lline)

for y in range(N):
    for x in range(N):
        if draw[y][x] == ' ':
            v= str((x,y))
            G[v] =list()
            if x-1 >= 0:
                if draw[y][x-1] == ' ':
                    G[v].append(str((x-1,y)))
            if y-1 >=0:
                if draw[y-1][x] == ' ':
                    G[v].append(str((x,y-1)))
            if x+1 < N:
                if draw[y][x+1] == ' ':
                    G[v].append(str((x+1,y)))
            if y+1 < N:
                if draw[y+1][x] == ' ':
                    G[v].append(str((x,y+1)))

s = str((0, 0))
d = Dijkstra(G, s)
print d[str((N-1,N-1))]