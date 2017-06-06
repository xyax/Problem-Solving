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

valMax = -1
graph = dict()
matrix = list()

largura, altura = map(int, raw_input().rstrip('\n').split())
x, y = map(int, raw_input().rstrip('\n').split())

maisAltos = list()
for line in sys.stdin:
    m = map(ord, list(line.rstrip('\n')))
    valMax = max(valMax, max(m))
    matrix.append(m)

for l in xrange(altura):
    for c in xrange(largura):
        if matrix[l][c] == valMax:
            maisAltos.append(str((c, l)))
        graph[str((c, l))] = list()
        if l - 1 >= 0:
            peso = 1 + abs(matrix[l - 1][c] - matrix[l][c])
            graph[str((c, l))].append([str((c, l - 1)), peso])
        if l + 1 < altura:
            peso = 1 + abs(matrix[l + 1][c] - matrix[l][c])
            graph[str((c, l))].append([str((c, l + 1)), peso])
        if c - 1 >= 0:
            peso = 1 + abs(matrix[l][c - 1] - matrix[l][c])
            graph[str((c, l))].append([str((c - 1, l)), peso])
        if c + 1 < largura:
            peso = 1 + abs(matrix[l][c + 1] - matrix[l][c])
            graph[str((c, l))].append([str((c + 1, l)), peso])

d = Dijkstra(graph, str((x, y)))
distMaisAltos = list()
for el in maisAltos:
    distMaisAltos.append(d[a])
print min(distMaisAltos)