__author__ = 'xyax'

N = int(raw_input())
mapa = [[' ' for i in xrange(N)] for j in xrange(N)]

def quemMata(m, l, c, N):
    m[l] = ['_' for i in xrange(N)]
    for j in xrange(N):
        m[j][c] = '_'
    for i in range(l, N):
        for j in range(c, N):
            m[i][j] = '_'
    for i in range(l, -1, -1):
        for j in range(c, N):
            m[i][j] = '_'
    m[l][c] = '*'
    return m


def preencheRainhas(m, lin, col, p, N):
    fl, fc = lin, col
    col += 1
    lin += 2
    while(col<N & lin<N):
        mapa[lin][col] = '*'
        quemMata(m, lin, col, N)
        fl, fc = lin, col
        p += 1
        col +=1
        lin +=2
    return m, p, fl, fc


def encontraRainha(m, col, p, N):
    for i in range(N):
        if m[i][col] == ' ':
            m[i][col] = '*'
            m = quemMata(m, i, col, N)
            p += 1
            break
    return m, p, int(i), col

l, c = 1, 0
mapa[l][c] = '*'
p = 1
while(p<N):
    mapa, p, l, c = preencheRainhas(mapa, c, l, p, N)
    print p, l, c
    mapa, p, l, c = encontraRainha(mapa, c, p, N)

for i in xrange(N):
    print ''.join(mapa[i])
