__author__ = 'xyax'
import sys

grafo = dict()
for line in sys.stdin:
    v1, v2 = line.rstrip('\n').split()
    if(not(v1 in grafo)):
        grafo[v1] = list()
    grafo[v1].append(v2)
    if(not(v2 in grafo)):
        grafo[v2] = list()
    grafo[v2].append(v1)

cores = dict()
b = True
i = 1
cores[i] = list()
for v in grafo:
    if(not v in cores[i]):
        for x in cores[i]:
            if x in grafo[v]:
                b = False
                break
        if(not b):
            i += 1
            cores[i] = list()
        cores[i].append(v)
        b = True

print i