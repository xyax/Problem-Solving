__author__ = 'xyax'

x, y = map(abs, map(int, raw_input().split()))

def mdc(a, b):
    if b==0:
        return a
    else:
        return mdc(b, a%b)
z = min(x, y)
print mdc(x+y-z, z)