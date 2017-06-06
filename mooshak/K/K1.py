__author__ = 'xyax'
import sys

pals = []
d = dict()
semEspacos = raw_input()
for line in sys.stdin:
    pals.append(line.rstrip('\n'))

def frase(semEspacos, i, pals, d):
    se = semEspacos[:i]
    if se in pals:
        sol = []
        if i==len(semEspacos):
            sol.append(semEspacos)
        else:
            sol.append(se)
            suf = semEspacos[i:]
            sol += frase(suf, len(suf), pals)
        return sol
    return frase(semEspacos, i-1, pals)

print(' '.join(frase(semEspacos, len(semEspacos), pals, d)))