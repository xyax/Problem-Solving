__author__ = 'xyax'
import sys

def dist(a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    if a[0] == b[0]:
        return dist(a[1:], b[1:])
    else:
        return 1 + min(dist(a, b[1:]), dist(a[1:], b), dist(a[1:], b[1:]))


last = raw_input()
for line in sys.stdin:
    s = line.rstrip('\n')
    print dist(last, s)
    last = s
