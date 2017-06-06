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

origem = raw_input()
distancia = int(raw_input())

G1 = dict()
for line in sys.stdin:
    v1, v2 = line.rstrip().split()
    if not(v1 in G1.keys()):
        G1[v1] = list()
    G1[v1].append(v2)
    #caso o grafo nao seja orientado, temos que criar o arco no sentido contrario
    #||APAGAR CASO SEJA ORIENTADO
    if not(v2 in G1.keys()):
        G1[v2] = list()
    G1[v2].append(v1)

d = Dijkstra(G1, origem)
out = list()
for el in d:
    if d[el] == distancia:
        out.append(el)

out.sort()
if len(out)>0:
    print '\n'.join(out)