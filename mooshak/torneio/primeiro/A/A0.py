import sys

corrida = dict()
for line in sys.stdin:
    tempo, nome = line.split()
    t = int(tempo)
    if not(nome in corrida.keys()):
        corrida[nome] = list()
    corrida[nome].append(t)

tMin = 100000
tempos = dict()
for c in corrida.keys():
    best = corrida[c][0]
    for i in range(1, len(corrida[c])):
        t = corrida[c][i]-corrida[c][i-1]
        best = min(best, t)
    corrida[c].append(best)
    tMin = min(tMin, best)

vencedores = list()
for c in corrida.keys():
    if corrida[c][-1]==tMin:
        vencedores.append(c)
vencedores.sort()
for v in vencedores:
    print v