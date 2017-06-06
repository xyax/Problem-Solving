import sys
import operator

voltas = dict()
tMin = 1000000
camp = list()
for line in sys.stdin:
    tempo, piloto = line.split()
    t = int(tempo)
    if not(piloto in voltas.keys()):
        voltas[piloto] = t
        tDif = t
    else:
        tDif = t - voltas[piloto]
        voltas[piloto] = min( voltas[piloto], tDif)
    tMin = min(tMin, tDif)

for v in voltas.keys():
    print v, ': ', voltas[v]
for v in voltas.keys():
    if voltas[v] == tMin:
        camp.append(v)

for c in camp:
    print c