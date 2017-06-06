import sys

N = int(raw_input())
mapa = list()
for line in sys.stdin:
    mapa.append(map(int, list(line.rstrip('\n'))))

def ski(mapa, N, pos):
    if N == 1:
        e = c = d = mapa[-N][pos]
        if pos > 0:
            e = mapa[-N][pos-1]
        if pos < len(mapa)-1:
            d = mapa[-N][pos+1]
        return max(e, c, d)
    l = list()
    for i in xrange(len(mapa)):
        if i>0:
            l.append(ski(mapa, N-1, i-1))
        if i < len(mapa)-1:
            l.append(ski(mapa, N-1, i+1))
        l.append(ski(mapa, N-1, i))
    return max(l)

print ski(mapa, N, 2)