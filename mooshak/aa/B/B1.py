__author__ = 'xyax'
import sys
import operator

graph=dict()
compG=dict()
for sEdge in sys.stdin:
    lEdge=sEdge.split()
    v1=lEdge[0]
    v2=lEdge[1]
    if not(v1 in graph.keys()):
        graph[v1]=list()
        if not(v1==v2):
            graph[v1].append(v2)
    else:
        if not(v1==v2):
            graph[v1].append(v2)
    if not(v2 in graph.keys()):
        graph[v2]=list()
        if not(v1==v2):
            graph[v2].append(v1)
    else:
        if not(v1==v2):
            graph[v2].append(v1)

for k1 in graph.keys():
    for k2 in graph.keys():
        if not(k2 in graph[k1]) and not(k1==k2):
            if not(k1 in compG.keys()):
                compG[k1]=list()
                compG[k1].append(k2)
            else:
                compG[k1].append(k2)


sCompG=sorted(compG.items(), key=operator.itemgetter(0))
pares=set()
pares.add(sCompG[0][0])
print(pares[0])
print(sCompG)
#print sCompG[0][0], sCompG[0][1]
"""for elem in sCompG:
    for c in elem[1]:
        s1=min(elem[0], c)
        s2=max(elem[0], c)
        print s1, s2
        pares.add((s1, s2))

sPares=sorted(pares, key=operator.itemgetter(0))
print pares"""