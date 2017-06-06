__author__ = 'xyax'

x, y = map(abs, map(int, raw_input().split()))
r = 1
for i in range(2, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
        r = i
print r