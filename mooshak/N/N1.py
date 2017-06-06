__author__ = 'xyax'
import sys

res = 0
N = int(raw_input())
seqs = list()

for line in sys.stdin:
    seqs.append(map(int, line.rstrip('\n').split()))

def somaN(s, N):
    if s[0] == N or N == 0:
        return True
    if len(s) > 1:
        return somaN(s[1:], N-s[0]) or somaN(s[1:], N)
    return False

for s in seqs:
    if somaN(s, N):
        res += 1
print(res)