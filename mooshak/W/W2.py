__author__ = 'xyax'
import sys

G = dict()
nomes = list()
for line in sys.stdin:
    v1, v2 = line.rstrip().split()
    if(not v1 in G):
        G[v1] = list()
        nomes.append(v1)
    if(not v2 in G):
        G[v2] = list()
        nomes.append(v2)
    G[v1].append(v2)
    G[v2].append(v1)

nomes.sort()

def todasAsCores(cores, N, k, i):
    if(i==N):
        print cores
        cores = list()
    else:
        for j in xrange(k):
            cores[i] = j
            todasAsCores(cores, N, k, i+1)

N = len(nomes)
cores = [0]*N
for x in xrange(N):
    todasAsCores(cores, N, x, 0)