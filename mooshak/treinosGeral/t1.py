__author__ = 'xyax'
import sys

for line in sys.stdin:
    n1, n2= map(int, line.split())
    print type(n1), n1
    print type(n2), n2
