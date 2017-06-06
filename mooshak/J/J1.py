__author__ = 'xyax'
import sys
import difflib

last = raw_input()
for line in sys.stdin:
    dif = 0
    for s in difflib.ndiff(last, line):
        if s[0] == '+':
            dif += 1
    print(dif+1)
    last = line
