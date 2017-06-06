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
    n = len(p)
    if(todasIguais(p)):
        return n-1
    m = int(n/2)
    j = m
    for t in xrange(m+1):
        f = True
        for i in xrange(j):
            if j+i < n:
                f = f & (p[i] == p[j+i])
        if f:
            return n-j
        j +=1
    return 0

for pal in l:
    print pal+pal[calc(pal):]
