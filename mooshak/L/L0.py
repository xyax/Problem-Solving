__author__ = 'xyax'
# !/usr/bin/python

import sys
import operator

city = dict()
for street in sys.stdin:
    cross1 = street[0]
    if '\n' == street[-1]:
        cross2 = street[-2]
    else:
        cross2 = street[-1]
    if cross1 in city.keys():
        city[cross1] += 1
    else:
        city[cross1] = 1
    if not (cross1 == cross2):
        if cross2 in city.keys():
            city[cross2] += 1
        else:
            city[cross2] = 1

preOut=sorted(city.items(), key=operator.itemgetter(0))
out = sorted(preOut, key=operator.itemgetter(1))
for l in out:
    print l[0], l[1]