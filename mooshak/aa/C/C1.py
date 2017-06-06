__author__ = 'xyax'
import sys
from collections import deque

def BFS(G, v):
    q = deque()
    q.append(v)
    descobertos = list()
    descobertos.append(v)
    while len(q) > 0:
        ver = q.popleft()
        for vertice in G[ver]:
            if not(vertice in descobertos):
                q.append(vertice)
                descobertos.append(vertice)
    return descobertos

graph = dict()
for line in sys.stdin:
    v1, v2 = line.rstrip().split()
    if not v1 in graph:
        graph[v1] = list()
    graph[v1].append(v2)
    if not v2 in graph:
        graph[v2] = list()
    graph[v2].append(v1)



continentes = list()
for v in graph:
    l = BFS(graph, v)
    l.sort()
    continentes.append(l[0])

scont = set(continentes)
lcont = list(scont)
lcont.sort()
for out in lcont:
    print out