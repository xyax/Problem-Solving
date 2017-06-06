__author__ = 'xyax'
import sys

def dist(a, b, d):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    if (a, b) in d.keys():
        return d[(a, b)]
    if a[0] == b[0]:
        d[(a, b)] = dist(a[1:], b[1:], d)
    else:
        d[(a, b)] = 1 + min(dist(a, b[1:], d), dist(a[1:], b, d), dist(a[1:], b[1:], d))
    return d[(a, b)]

last = raw_input()
for line in sys.stdin:
    s = line.rstrip('\n')
    d = dict()
    print(dist(last, s, d))
    last = s
