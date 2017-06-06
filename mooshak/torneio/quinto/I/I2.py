__author__ = 'xyax'
import sys

l = list()
for line in sys.stdin:
    l.append(line.rstrip('\n'))

def todasIguais(p):
    a = p[0]
    for e in p:
        if not e == a:
            return False
    return True

def calc(p):
    r = 0
    n = len(p)
    if todasIguais(p):
        return n-1
    m = int(n/2)
    j = m
    for i in xrange(m):
        if p[i] == p[j]:
            r += 1
        else:
            return r
    return r

for pal in l:
    print pal+pal[calc(pal):]