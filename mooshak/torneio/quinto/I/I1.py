__author__ = 'xyax'
import sys

l = list()
for line in sys.stdin:
    l.append(line.rstrip('\n'))

def calc(pal):
    r=0
    n = len(pal)
    for i in xrange(n):
        if pal[i] == pal[-(i+1)]:
            r+=1
        else:
            return r
    return r-1

for p in l:
    print p+p[calc(p):]
