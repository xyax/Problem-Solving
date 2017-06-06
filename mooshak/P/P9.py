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
                spTree[v] = u
    return dist, spTree


N = int(raw_input())
draw = list()
G = dict()
for line in sys.stdin:
    lline = list(line)
    if lline[-1] == '\n':
        lline.pop()
    draw.append(lline)

for y in range(N):
    for x in range(N):
        if draw[y][x] == ' ':
            v= str((x,y))
            G[v] =list()
            if x-1 >= 0:
                if draw[y][x-1] == ' ':
                    G[v].append(str((x-1,y)))
            if y-1 >=0:
                if draw[y-1][x] == ' ':
                    G[v].append(str((x,y-1)))
            if x+1 < N:
                if draw[y][x+1] == ' ':
                    G[v].append(str((x+1,y)))
            if y+1 < N:
                if draw[y+1][x] == ' ':
                    G[v].append(str((x,y+1)))

s = str((0, 0))
d, sp = Dijkstra(G, s)
for el in sp:
    print el, ': ', sp[el]
par = str((N-1,N-1))
print d[par]
caminho = list()
while not sp[par] == '-':
    caminho.append(par)
    par = sp[par]
caminho.append(s)
caminho.reverse()
for c in caminho:
    print c