__author__ = 'xyax'
N = int(raw_input())

mapa = [['[ ]' for i in xrange(N)] for j in xrange(N)]
mapa[1][0] = '[*]'
l, c = 1, 0
if (N%2) == 0:
    for x in xrange(N):
        if l >= N:
            aux = l - N - 1
        else:
            aux = l
        mapa[aux][c] = '[*]'
        l = aux + 2
        c +=1
else:
    for x in xrange(N):
        if l >= N:
            aux = l - N
        else:
            aux = l
        mapa[aux][c] = '[*]'
        l = aux + 2
        c +=1


for a in xrange(N):
    print ''.join(mapa[a])