__author__ = 'xyax'
import sys

res = 0
N = int(raw_input())
seqs = list()

for line in sys.stdin:
    seqs.append(map(int, line.rstrip('\n').split()))

def somaN(s, N, d):
    k = (len(s), N)
    if s[0] == N or N == 0:
        d[k] = True
    if not(k in d):
        if len(s) > 1:
            d[k] = somaN(s[1:], N-s[0], d) or somaN(s[1:], N, d)
        else:
            d[k] = False
    return d

for s in seqs:
    d = dict()
    mem = somaN(s, N, d)
    print(mem)
    if True in mem.values():
        res += 1
print(res)