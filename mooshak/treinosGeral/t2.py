__author__ = 'xyax'
import sys

dist = {'a': 11,
        'b': 4,
        'c': 3,
        'd': 10,
        'f': 7}

q = ['a', 'c', 'd']
vert= str()
m = sys.maxint
for e in q:
    if m > dist[e]:
        m= dist[e]
        vert = e
print(vert)