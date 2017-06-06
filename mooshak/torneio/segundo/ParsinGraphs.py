__author__ = 'xyax'
import sys

#leitura de grafo nao pesado para dicionario de listas
#v1 v2
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

#leitura de um grafo pesado para dicionario de listas
#v1 v2  peso
G2 = dict()
for line in sys.stdin:
    v1, v2, p = line.rstrip().split()
    peso = int(p)
    if not(v1 in G2.keys()):
        G2[v1] = list()
    G2[v1].append([v2, peso])

#leitura de um grafo para matriz de adjacencias
#v1 v2 peso
G3 = dict()
for line in sys.stdin:
    v1, v2, p = line.rstrip().split()
    peso = int(p)
    if not(v1 in G3.keys()):
        G3[v1] = dict()
    G3[v1][v1] = 0
    G3[v1][v2] = peso
    #caso o grafo nao seja orientado, temos que criar o arco no sentido contrario
    #||APAGAR CASO SEJA ORIENTADO
    if not(v2 in G3.keys()):
        G3[v2] = dict()
    G3[v2][v2] = 0
    G3[v2][v1] = peso

#leitura de um mapa
G4 = dict()
matrix = list()
for line in sys.stdin:
    linha = list(line.rstrip())
    matrix.append(linha)
linhas, colunas = len(matrix), max(map(len, matrix))
#do mapa para grafo de dicionario com listas
for l in xrange(linhas):
    for c in xrange(colunas):
        if matrix[l][c]:
            G4[(c,l)] = list()
            if l-1 >= 0:
                if matrix[l-1][c]:
                    G4[(c,l)].append((c,l-1))
            if l+1 < linhas:
                if matrix[l+1][c]:
                    G4[(c,l)].append((c,l+1))
            if c-1 >= 0:
                if matrix[l][c-1]:
                    G4[(c,l)].append((c-1,l))
            if c+1 < colunas:
                if matrix[l][c+1]:
                    G4[(c,l)].append((c+1,l))

#leitura de varios vertices adjacentes na mesma linha para um dicionario de listas
G5 = dict()
for line in sys.stdin:
    lline = line.rstrip().split()
    for v1 in lline:
        for v2 in lline:
            if not v1 in G5:
                G5[v1] = list()
            if not v1 == v2 and not v2 in G5[v1]:
                G5[v1].append(v2)
