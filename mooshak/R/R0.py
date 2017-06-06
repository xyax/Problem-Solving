__author__ = 'xyax'
import sys

inteiros = list()
for line in sys.stdin:
    inteiros.append(int(line))
for i in inteiros:
    print bin(i)[2:]