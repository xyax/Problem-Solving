__author__ = 'xyax'
import sys
from collections import deque

maior = 0
planeta = dict()
for line in sys.stdin:
    lline = line.split()
    for i in range(len(lline)):
        s1 = lline[i]
        if not(s1 in planeta.keys()):
            planeta[s1] = list()
        for j in range(len(lline)):
            if not(i==j):
                s2 = lline[j]
                planeta[s1].append(s2)

for pais in planeta.keys():
    q = deque([pais])
    vis = [pais]
    while len(q) > 0:
        v = q.popleft()
        for w in planeta[v]:
            if not(w in vis):
                q.append(w)
                vis.append(w)
    maior = max(maior, len(vis))

print maior