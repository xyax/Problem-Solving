# !/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xyax'
import sys
import operator

turma=dict()
for sAluno in sys.stdin:
    lAluno=sAluno.split()
    if not(lAluno[0] in turma.keys()):
        turma[lAluno[0]]=int(lAluno[1])
    else:
        turma[lAluno[0]]+=int(lAluno[1])

preOut=sorted(turma.items(), key=operator.itemgetter(0))
out=sorted(preOut, key=operator.itemgetter(1), reverse=True)

for a in out:
    print a[0], a[1]