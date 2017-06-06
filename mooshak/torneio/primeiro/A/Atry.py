__author__ = 'xyax'

def toSec(h, m, s):
    return h*3600 + m*60 + s

def toHour(s):
    m, s = s / 60, s % 60
    h, m = m / 60, m % 60
    return (h, m, s)

print toHour(3685)
"""
20 Alonso
20 Rosberg
25 Hamilton
35 Rosberg
50 Alonso
55 Hamilton
70 Hamilton
80 Rosberg
70 Alonso
100 Alonso
120 Hamilton
"""