__author__ = 'xyax'
from collections import deque

def BFS(G, v):
    #'q' e uma queue que tem os vertices que se encontram na orla a qualquer instante
    q = deque()
    q.append(v)
    #'descobertos' e uma lista que contem todos os vertices acessiveis a partir do vertice inicial v
    descobertos = [v]
    #a condicao deste ciclo testa se ainda existem vertices na orla
    while len(q) > 0:
        #tira o vertice mais antigo da orla e coloca em v
        v = q.popleft()
        #percorre todos os vertices adjacentes de v
        for vertice in G[v]:
            #se o vertice ainda nao foi descoberto, insere-o em 'descobertos' e na orla
            if not(vertice in descobertos):
                q.append(vertice)
                descobertos.append(vertice)
                #caso queiramos construir a "spanning tree" basta dizer que o pai do vertice 'vertice' e o vertice v
                #spTree[vertice] = v
    return descobertos