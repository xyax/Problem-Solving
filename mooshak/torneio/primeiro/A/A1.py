import sys
import operator

def toSec(h, m, s):
    return h*3600 + m*60 + s

def toHour(s):
    m, s = s / 60, s % 60
    h, m = m / 60, m % 60
    return (h, m, s)

corridas = dict()
for line in sys.stdin:
    nome, tempo = line.split()
    h, m, s = map(int, tempo.split(':'))
    if not(nome in corridas.keys()):
        corridas[nome] = 0
    corridas[nome] += toSec(h, m, s)

out = sorted(corridas.items(), key=operator.itemgetter(0))
out.sort(key=operator.itemgetter(1))
for o in out:
    ho, mo, so = toHour(o[1])
    print "%s %d:%d:%d" % (o[0], ho, mo, so)