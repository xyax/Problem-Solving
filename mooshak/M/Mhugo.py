#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Fazer matriz de adjacência
e percorrer com Floyd-Warshall
1 let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
2 for each vertex v
3    dist[v][v] ← 0
4 for each edge (u,v)
5    dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
6 for k from 1 to |V|
7    for i from 1 to |V|
8       for j from 1 to |V|
9          if dist[i][j] > dist[i][k] + dist[k][j] 
10             dist[i][j] ← dist[i][k] + dist[k][j]
11         end if
'''
import sys

entrada=[]
cidade=dict()

for line in sys.stdin:
	rua = ''.join(line.rsplit())
	comp=len(rua)
	first=rua[0]
	last=rua[-1]
	igual= True
 	if first==last:
 		igual = False
	if igual:
 		if first in cidade:
 			primeiros=[x[0] for x in cidade[first]] #lista com os a's dos pares (a,b)
 			#print primeiros
 			if last in primeiros:
 				indice=primeiros.index(last)
 				segundos=[x[1] for x in cidade[first]]
 				#print segundos
 				if (segundos[indice]>comp):
 					cidade[first].append((last,comp))
 			else:
 				cidade[first].append((last,comp))
 		if first not in cidade:
 			cidade[first]=[]
 			cidade[first].append((last,comp))
 		if last in cidade:
 			primeiros=[x[0] for x in cidade[last]]
 			if first in primeiros:
 				indice=primeiros.index(first)
 				segundos=[x[1] for x in cidade[last]]
 				if (segundos[indice]>comp):
 					cidade[last].append((first,comp))
 			else:
 				cidade[last].append((first,comp))
 		if last not in cidade:
 			cidade[last]=[]
 			cidade[last].append((first,comp))


#IMPRESSÃO DA CIDADE

'''for key in sorted(cidade):
	print key,
	for elem in cidade[key]:
		print elem,
	print'''

#IMPRESSÃO DA CIDADE

#Passar chaves e valores do dict para int
numerovertices=0
vertices=[]
for elem in entrada:
	first=elem[0]
	last=elem[len(elem)-1]
	if first not in vertices:
		vertices.append(first)
		numerovertices+=1
	if last not in vertices:
		vertices.append(last)
		numerovertices+=1
#print numerovertices
novacidade=dict()
i=0
atribuidos=dict()
for key in sorted(cidade):
	if key not in atribuidos:
		atribuidos[key]=i
		i+=1

#print atribuidos

for key in cidade:
	novacidade[atribuidos[key]]=[]
	for elem in cidade[key]:
		novacidade[atribuidos[key]].append((atribuidos[elem[0]],elem[1]))
#print "NOVACIDADE"
#print novacidade

dist = [[100 for x in range(numerovertices)] for x in range(numerovertices)]
'''
for lista in dist:
	for elem in lista:
		print elem,
	print
'''
for i in xrange(numerovertices):
	for j in xrange(numerovertices):
		if i==j:
			dist[i][j]=0
'''
for lista in dist:
	for elem in lista:
		print elem,
	print
'''
for key in novacidade:
	for elem in novacidade[key]:
		dist[key][elem[0]]=elem[1]
'''
print
for lista in dist:
	for elem in lista:
		print elem,
	print
'''
for k in xrange(numerovertices):
    for i in xrange(numerovertices):
       for j in xrange(numerovertices):
          if (dist[i][k]+dist[k][j]<dist[i][j]):
          	dist[i][j]=dist[i][k]+dist[k][j]
        
'''
for lista in dist:
	for elem in lista:
		print elem,
	print
'''
maior=0
for lista in dist:
	for elem in lista:
		if elem>maior:
			maior=elem


print maior










