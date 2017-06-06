__author__ = 'xyax'
import sys
import operator
from math import sqrt

distancias = dict()
for line in sys.stdin:
    l = map(int, line.split())
    d = sqrt(sum(map(lambda x: x ** 2, l)))
    if not(d in distancias.keys()):
        distancias[d] = list()
    distancias[d].append(l)

out = sorted(distancias.items(), key=operator.itemgetter(0))
for o in out:
    reversed(o[1])
    print '\n'.join(map(lambda x: ' '.join(map(str, x)), o[1]))

