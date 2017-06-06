__author__ = 'xyax'
import sys

graph=dict()
for line in sys.stdin:
    if line == '':
        break
    
    lline=list()
    lline=line.split()
    s1, s2=lline[0], lline[1]
    if not(s1 in graph.keys()):
        graph[s1]=list()
    if not(s2 in graph[s1]):
        graph[s1].append(s2)
    if not(s2 in graph.keys()):
        graph[s2]=list()
    if not(s1 in graph[s2]):
        graph[s2].append(s1)

sGraph=set()
for v1 in graph.keys():
    for v2 in graph.keys():
        if not(v1==v2) and not(v2 in graph[v1]):
            p= [v1, v2]
            p.sort()
            sGraph.add((p[0], p[1]))

gComp=list(sGraph)
gComp.sort()
for out in gComp:
    print out[0], out[1]
