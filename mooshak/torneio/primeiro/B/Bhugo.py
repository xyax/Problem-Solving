#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import operator
from math import sqrt

def dist(l):
	dista=0
	for elem in l:
		dista+=(elem)**2
	dista=sqrt(dista)
	return dista

pontos= dict()

#a key é o ponto
#o value é um par em que x é a posição e y é a distância
posicao=0
for line in sys.stdin:
	#print line,
	l=line.split()
	posicao+=1
	#print l
	novalista=map(int,l)
	#print novalista
	valor=dist(novalista)
	#print valor
	if (valor,posicao) not in pontos:
		pontos[(valor,posicao)]=novalista


novospontos={}
for key in pontos:
	if key[0] in novospontos:
		novospontos[key[0]].append(key[1])
	if key[0] not in novospontos:
		novospontos[key[0]]=[]
		novospontos[key[0]].append(key[1])

for key in novospontos:
	novospontos[key].sort(reverse=True)

for key in sorted(novospontos):
	#print key,
	#print novospontos[key]
	for elem in novospontos[key]:
		print ' '.join(map(str,pontos[(key,elem)])),''

#keys = pontos.keys()
#print keys
#for i, elem in enumerate(keys):
#	print i,
#	print elem
#	if 
#for i, k in enumerate(keys):
#	print i,
#	print k
#	if ()
#for key in sorted(pontos):
#	print key,
#	print pontos[key]
#sPontos = sorted(pontos.items(),key=operator.itemg)
#for i, k in enumerate(sorted(pontos)):
#	print i,
#	print k
#	print ' '.join(map(str, pontos[k]))

	#if pontos[k]==pontos[k[i+1]]:
	#	print "OLA"
