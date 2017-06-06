__author__ = 'xyax'
import sys
import operator

def Dijkstra(G, source):
    #inf funciona como "infinito"
    inf = sys.maxint
    #'dist' vai guardar todas as distancias de 'source' a qualquer vertice do grafo
    dist = dict()
    #'spTree' vai ser a spanning tree de 'source' ate qualquer vertice
    spTree = dict()
    #'q' guarda a qualquer instante os vertices ainda nao visitados
    q = list()
    #inicializa 'dist', 'spTree' com valores default e insere todos
    #os vertices em 'q'
    for v in G.keys():
        dist[v] = inf
        spTree[v] = '-'
        q.append(v)
    #a distancia de 'source' a ele proprio e 0
    dist[source] = 0
    #agora vamos visitar todos os vertices
    while len(q) > 0:
        #fazer sair de 'q' o vertice mais proximo da 'source' que ainda nao foi visitado
        laux = [(e, dist[e]) for e in q]
        laux.sort(key=operator.itemgetter(1))
        u = q.pop(q.index(laux[0][0]))
        #vamos percorrer todos os vertices adjacentes de u
        for v in G[u]:
            #caso grafo seja pesado substituir o 1 pelo peso respetivo
            alt = dist[u] +v[1]
            #se a distancia alternativa for mais curta, atualiza
            if alt < dist[v[0]]:
                dist[v[0]] = alt
                spTree[v[0]] = u
    return dist, spTree

G = dict()
partida, chegada = raw_input().split()
for line in sys.stdin:
    v1, v2, p = line.split()
    peso = int(p)
    if not(v1 in G.keys()):
        G[v1] = list()
    G[v1].append([v2, peso])
    if not(v2 in G.keys()):
        G[v2] = list()
    G[v2].append([v1, peso])

d, sp = Dijkstra(G, partida)
print(d[chegada])

for el in sp:
    print el, ': ', sp[el]

caminho = list()
while not sp[chegada] == '-':
    caminho.append(chegada)
    chegada = sp[chegada]
caminho.append(partida)
caminho.reverse()
print '\n'.join(caminho)