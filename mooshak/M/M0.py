__author__ = 'xyax'
import sys

def FloydWarshall(G):
    inf = sys.maxint
    for a in G.keys():
        for b in G.keys():
            if not(b in G[a].keys()):
                G[a][b] = inf
                G[b][a] = inf

    for k in G.keys():
        for i in G.keys():
            for j in G.keys():
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    return G

G = dict()
for rua in sys.stdin:
    rua = rua.rstrip('\n')
    v1, v2, peso = rua[0], rua[-1], len(rua)
    if not(v1 in G):
        G[v1] = dict()
    G[v1][v1] = 0
    if not(v2 in G[v1]):
        G[v1][v2] = peso
    else:
        G[v1][v2] = min(G[v1][v2], peso)
    if not(v2 in G):
        G[v2] = dict()
    G[v2][v2] = 0
    if not(v1 in G[v2].keys()):
        G[v2][v1] = peso
    else:
        G[v2][v1] = min(G[v2][v1], peso)

G2 = FloydWarshall(G)
m = 0
for e in G2:
    m = max(m, max(G2[e].values()))
print m