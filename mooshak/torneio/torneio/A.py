__author__ = 'xyax'
import sys

tMin = sys.maxint
corrida = dict()
for line in sys.stdin:
    tempo, nome = line.split()
    t = int(tempo)
    if not(nome in corrida.keys()):
        corrida[nome] = t, t
    else:
        corrida[nome] = min(corrida[nome][0], t - corrida[nome][1]), t
        tMin = min(corrida[nome][0], tMin)

vencedores = list()
for c in corrida.keys():
    if corrida[c][0] == tMin:
        vencedores.append(c)

vencedores.sort()
print '\n'.join(vencedores)
