__author__ = 'xyax'
import sys

grafo = dict()
nomes = list()
for line in sys.stdin:
    v1, v2 = line.rstrip().split()
    if(not v1 in grafo):
        grafo[v1] = list()
        nomes.append(v1)
    if(not v2 in grafo):
        grafo[v2] = list()
        nomes.append(v2)
    grafo[v1].append(v2)
    grafo[v2].append(v1)

def todasAsCores(cores, N, k, i):
    if(i==N):
        return True
    for j in xrange(1, k+1):
        cores[i] = j
        flag = True
        for v in grafo[nomes[i]]:
            if cores[nomes.index(v)]:
                flag = False
                break
        if flag:
            todasAsCores(cores, N, k, i+1)

k = 1
cores = [-1]
while(not todasAsCores(cores, len(nomes), k, 0)):
    k += 1
    cores = [-1]*k
print k