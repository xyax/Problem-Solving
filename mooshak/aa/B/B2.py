__author__ = 'xyax'
import sys

lVertices=list()
graph=dict()

for sEdge in sys.stdin:
    if sEdge=='\n':
        break
    lEdge=sEdge.split()
    v1=lEdge[0]
    v2=lEdge[1]
    if lVertices.count(v1)==0:
        lVertices.append(v1)
        graph[v1]=list()
        graph[v1].append(v2)
    else:
        graph[v1].append(v2)
    if lVertices.count(v2)==0:
        lVertices.append(v2)
        graph[v2]=list()
        graph[v2].append(v1)
    else:
        graph[v2].append(v1)

gComp=dict()
for vert1 in lVertices:
    for vert2 in lVertices:
        if not(vert1==vert2) and graph[vert1].count(vert2)==0:
            if not(vert1 in gComp.keys()):
                gComp[vert1]=list()
                gComp[vert1].append(vert2)
            else:
                gComp[vert1].append(vert2)

sAllE=set()
for v in lVertices:
    for e in gComp[v]:
        p=[v, e]
        p.sort()
        sAllE.add((p[0], p[1]))

lAllE=list(sAllE)
lAllE.sort()

for out in lAllE:
    print out[0], out[1]

