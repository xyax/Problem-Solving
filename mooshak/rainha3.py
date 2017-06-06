__author__ = 'xyax'

N = int(raw_input())
tabuleiro = [['[ ]' for i in xrange(N)] for j in xrange(N)]
linha = 1
coluna = 0
rainhas = 0


def mata(t, l, c, N):
    tl = l - 1
    tc = c + 1
    while (tl >= 0) & (tc < N):
        t[tl][tc] = '[X]'
        tl -= 1
        tc += 1
    tl = l + 1
    tc = c + 1
    while (tl < N) & (tc < N):
        t[tl][tc] = '[X]'
        tl += 1
        tc += 1
    tc = c + 1
    while tc < N:
        t[l][tc] = '[X]'
        tc += 1
    return t


def encontraLinha(t, c, N):
    l = 0
    while t[l][c] == '[X]':
        l += 1
    return l


def preencheRainhas(t, l, c, r, N):
    l += 2
    c += 1
    while (r <= N) & (l < N) & (c < N):
        t[l][c] = '[Q]'
        r += 1
        t = mata(t, l, c, N)
        l += 2
        c += 1
    return t, l, c - 1, r

def enterraMortos(t, N):
    for i in xrange(N):
        for j in xrange(N):
            if t[i][j] == '[X]':
                t[i][j] = '[ ]'
    return t

def impremeTabuleiro(t, N):
    for i in xrange(N):
        print(''.join(t[i]))

tabuleiro[linha][coluna] = '[Q]'
rainhas += 1
tabuleiro = mata(tabuleiro, linha, coluna, N)
while (rainhas < N) & (coluna < N):
    if (linha >= N) & ((coluna + 1) < N):
        coluna += 1
        linha = encontraLinha(tabuleiro, coluna, N)
        tabuleiro[linha][coluna] = '[Q]'
        rainhas += 1
        tabuleiro = mata(tabuleiro, linha, coluna, N)
    if rainhas <= N:
        tabuleiro, linha, coluna, rainhas = preencheRainhas(tabuleiro, linha, coluna, rainhas, N)

tabuleiro = enterraMortos(tabuleiro, N)
impremeTabuleiro(tabuleiro, N)
