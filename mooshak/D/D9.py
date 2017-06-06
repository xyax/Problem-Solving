__author__ = 'xyax'
import sys

comandos = list()
for line in sys.stdin:
    comandos.append(line.split())

out = list()
for cmd in comandos:
    x = y = x0 = y0 = x1 = y1 = vx = 0
    vy = 1
    for c in cmd:
        if c == 'A':
            x += vx
            y += vy
        elif c == 'D':
            aux = vx
            vx = vy
            vy = aux * (-1)
        elif c == 'E':
            aux = vy
            vy = vx
            vx = aux * (-1)
        else:
            quadrado = ((x0, y0), (x1, y1))
            out.append(quadrado)
            break
        x0 = min(x0, x)
        y0 = min(y0, y)
        x1 = max(x1, x)
        y1 = max(y1, y)

for o in out:
    print "(%d,%d) (%d,%d)" % (o[0][0], o[0][1], o[1][0], o[1][1])