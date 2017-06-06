#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import operator

def Dijkstra(G, source):
    #inf funciona como "infinito"
    inf = sys.maxint
    #'dist' vai guardar todas as distancias de 'source' a qualquer vertice do grafo
    dist = dict()
    #'q' guarda a qualquer instante os vertices ainda nao visitados
    q = list()
    #inicializa 'dist', 'spTree' com valores default e insere todos
    #os vertices em 'q'
    for v in G.keys():
        dist[v] = inf
        q.append(v)
    #a distancia de 'source' a ele proprio e 0
    dist[source] = 0
    #agora vamos visitar todos os vertices
    while len(q) > 0:
        #'m' e 'vert' sao variaveis temporarias para descobrir
        #o vertice mais proximo da 'source' que ainda nao foi visitado
        laux = [(e, dist[e]) for e in q]
        laux.sort(key=operator.itemgetter(1))
        u = q.pop(q.index(laux[0][0]))
        #vamos percorrer todos os vertices adjacentes de u
        for v in G[u]:
            #caso grafo seja pesado substituir o 1 pelo peso respetivo
            alt = dist[u] +1
            #se a distancia alternativa for mais curta, atualiza
            if alt < dist[v]:
                dist[v] = alt
    return dist

N = int(raw_input())
matrix = list()
for line in sys.stdin:
    matrix.append(list(line.rstrip('\n')))
x, y= -1, -1
saidas = list()
graph = dict()
for l in xrange(N):
    for c in xrange(N):
        if (l==0 or c==0 or l==N-1 or c==N-1) and (matrix[l][c] == ' ' or matrix[l][c]=='R'):
            saidas.append((c,l))
        if matrix[l][c]=='R':
            x, y= c, l
        if matrix[l][c] == ' ' or matrix[l][c]=='R':
            graph[(c,l)] = list()
            if l+1<N:
                if matrix[l+1][c]==' ' or matrix[l+1][c]=='R':
                    graph[(c,l)].append((c,l+1))
            if l-1>=0:
                if matrix[l-1][c]==' ' or matrix[l-1][c]=='R':
                    graph[(c,l)].append((c,l-1))
            if c+1<N:
                if matrix[l][c+1]==' ' or matrix[l][c+1]=='R':
                    graph[(c,l)].append((c+1,l))
            if c-1>=0:
                if matrix[l][c-1]==' ' or matrix[l][c-1]=='R':
                    graph[(c,l)].append((c-1,l))

d = Dijkstra(graph, (x,y))
inf = sys.maxint
out = inf
for s in saidas:
    if not d[s]==inf:
        out = min(out, d[s])
print(out)