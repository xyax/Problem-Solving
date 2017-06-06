__author__ = 'xyax'

import sys

cmds= list()

for line in sys.stdin:
    cmds.append(line.split())

for cmd in cmds:
    x= y= x0= x1= y0= y1= vx= 0
    vy= 1
    for c in cmd:
        if c=='A':
            x+=vx
            y+=vy
            x0= min(x0, x)
            y0= min(y0, y)
            x1= max(x1, x)
            y1= max(y1, y)
        elif c=='D':
            aux= vx
            vx= vy
            vy= aux*(-1)
        elif c=='E':
            aux=vx
            vx= vy*(-1)
            vy= aux
        else:
            print "(%d,%d) (%d,%d)" % (x0, y0, x1, y1)