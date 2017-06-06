__author__ = 'xyax'

import sys

p= 0, 0
v= 0, 1
inf= sup= 0, 0
area= inf, sup
def parsing():
    com= list()
    for line in sys.stdin:
        com.append(line.split())
    return com

def updateArea(p, area):
    inf= min(area[0][0], p[0]), min(area[0][1], p[1])
    sup= max(area[1][0], p[0]), max(area[1][1], p[1])
    area= inf, sup
    return area

def printArea(area):
    print "(%d,%d) (%d,%d)" % (area[0][0], area[0][1], area[1][0], area[1][1])

def calculateArea(cmd, p, area):
    for c in cmd:
        if c=='A':
            p+= v
        elif c=='D':
            v= v[1], v[0]*(-1)
            p+=v
        elif c=='E':
            v= v[1]*(-1), v[0]
            p+=v
        else: printArea(area)
        area= updateArea(p, area)

cmds= parsing()
calculateArea(cmds, p, area)