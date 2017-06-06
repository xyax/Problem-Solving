__author__ = 'xyax'
import sys

g= dict()
for line in sys.stdin:
    a, b = line.split()
    if not(a in g.keys()):
        g[a] = list()
    g[a].append(b)
    if not(b in g.keys()):
        g[b] = list()
    g[b].append(a)

gc = dict()
for x in g.keys():
    for y in g.keys():
        if not(x == y) and not(y in g[x]):
            if not(x in gc.keys()):
                gc[x] = list()
            gc[x].append(y)

sgc = set()
for k in gc.keys():
    for e in gc[k]:
        lk = [k, e]
        lk.sort()
        sgc.add((lk[0], lk[1]))

lgc = list(sgc)
lgc.sort()
for o in lgc:
    print ' '.join(o)