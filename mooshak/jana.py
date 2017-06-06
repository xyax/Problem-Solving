__author__ = 'xyax'
import sys

lin = list()
for line in sys.stdin:
    lin.append(map(float, line.rstrip().split()))
