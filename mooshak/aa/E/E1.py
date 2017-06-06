__author__ = 'xyax'
import sys

moedas = []
N = int(raw_input())
for num in sys.stdin:
    moedas.append(int(num.rstrip('\n')))

def troco(N, moedas, d):
    if N == 0:
        return 0
    out = [10000]
    out.append(map((lambda m: 1+troco((N-m), moedas, d)), filter((lambda m: m<=N), moedas)))
    return min(out)

d = dict()
print(troco(N, moedas, d))