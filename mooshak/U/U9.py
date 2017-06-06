__author__ = 'xyax'
import sys
import operator

pals = dict()
for line in sys.stdin:
    lline = line.split()
    for l in lline:
        if not(l in pals.keys()):
            pals[l] = 0
        pals[l] += 1

out = sorted(pals.items(), key=operator.itemgetter(0))
out.sort(key=operator.itemgetter(1), reverse=True)
for o in out:
    print "%s: %s" % (o[0], o[1])