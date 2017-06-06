__author__ = 'xyax'

l = map(int, raw_input().split())
acum = smax =0
for x in l:
    acum += x
    acum = max(0, acum)
    smax = max(smax, acum)

elmax = max(l)
if elmax < 0:
    print(elmax)
else:
    print(smax)