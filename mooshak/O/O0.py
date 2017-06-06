__author__ = 'xyax'
import sys

binarios = list()
for line in sys.stdin:
    binarios.append(int(line, base = 2))
for b in binarios:
    print int(b)