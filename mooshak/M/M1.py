__author__ = 'xyax'
import sys
from collections import deque

maiorPeso = 0
cidade = dict()
for rua in sys.stdin:
    v1, v2 = rua[0], rua[-2]
    peso = len(rua)
    if not(v1 in cidade.keys()):
        cidade[v1] = [(v2, peso)]

for r in cidade.keys():
    p = 0
    q = deque([r])
    vis = [r]
    while len(q) > 0:
        v = q.popleft()
        if v in cidade.keys():
            laux = map(lambda k: k[0], cidade[v])
            for w in laux:
                if not(w in vis):
                    q.append(w)
                    vis.append(w)
                    p += cidade[v][laux.index(w)][1]
    maiorPeso = max(maiorPeso, p)

print maiorPeso