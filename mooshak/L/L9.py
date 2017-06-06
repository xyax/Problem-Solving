__author__ = 'xyax'
import sys
import operator

g= dict()
for rua in sys.stdin:
    a = rua[0]
    if rua[-1] == '\n':
        b = rua[-2]
    else:
        b = rua[-1]
    if not(a in g.keys()):
        g[a] = 1
    else:
        g[a] += 1
    if not(b in g.keys()):
        g[b] = 1
    else:
        g[b] += 1
    if a == b:
        g[a] -= 1


out = sorted(g.items(), key=operator.itemgetter(0))
out.sort(key=operator.itemgetter(1))
for o in out:
    print o[0], o[1]