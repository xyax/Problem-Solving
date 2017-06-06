# !/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xyax'

import sys
import operator

pals=dict()

for sLine in sys.stdin:
    lLine=sLine.split()
    for l in lLine:
        if not(l in pals.keys()):
            pals[l]=1
        else:
            pals[l]+=1

preOut=sorted(pals.items(), key=operator.itemgetter(0))
out=sorted(preOut, key=operator.itemgetter(1), reverse=True)

for p in out:
    print "%s: %d" % (p[0], p[1])