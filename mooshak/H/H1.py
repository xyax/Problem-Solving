__author__ = 'xyax'

l = map(int, raw_input().split())
sMax = max(l)
acum = 0
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        sMax = max(sMax, sum(l[i:j]))

print sMax