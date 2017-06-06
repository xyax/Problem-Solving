__author__ = 'xyax'
import sys

def Dijkstra(G, source):
    inf = sys.maxint
    dist = dict()
    q = list()
    for v in G.keys():
        dist[v] = inf
        q.append(v)
    dist[source] = 0
    while len(q) > 0:
        vert= str()
        m = inf
        for e in q:
            if m > dist[e]:
                m= dist[e]
                vert = e
        u = q.pop(q.index(vert))
        for v in G[u]:
            alt = dist[u] + v[1]
            if alt < dist[v[0]]:
                dist[v[0]] = alt
    return dist

G = dict()
partida, chegada = raw_input().split()
for line in sys.stdin:
    v1, v2, p = line.split()
    peso = int(p)
    if not(v1 in G.keys()):
        G[v1] = list()
    G[v1].append([v2, peso])
    if not(v2 in G.keys()):
        G[v2] = list()
    G[v2].append([v1, peso])

d = Dijkstra(G, partida)
print(d[chegada])