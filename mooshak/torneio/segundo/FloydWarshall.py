__author__ = 'xyax'
import sys

def FloydWarshall(G):
    #define inf como o maximo inteiro possivel
    inf = sys.maxint
    #a e b sao duas variaveis que percorrem todos os vertices do grafo
    for a in G.keys():
        for b in G.keys():
            #preenche a "infinito" todas as distancias de pares de vertices nao adjacentes
            if not(b in G[a].keys()):
                G[a][b] = inf
                #caso seja nao orientado
                #||APAGAR CASO SEJA ORIENTADO
                G[b][a] = inf

    #k, i, j percorrem todos os vertices do grafo
    for k in G.keys():
        for i in G.keys():
            for j in G.keys():
                #se ao passar por k, a distancia entre i e j e menor, entao atualiza a menos distancia
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    return G