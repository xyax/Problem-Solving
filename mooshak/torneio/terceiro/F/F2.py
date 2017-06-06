import sys

numeros = list()
v = int(raw_input())
for line in sys.stdin:
    numeros.append(line.rstrip('\n'))

def bate(v, pre, suf, d):
    if (v, pre, suf) in d.keys():
        return d[(v, pre, suf)]
    if not pre:
        if not suf:
            d[(v, pre+suf)] = False
        elif v == int(suf):
            d[(v, pre, suf)] = True
        else:
            d[(v, pre, suf)] = bate(v, suf[0], suf[1:], d) or bate(v-int(suf[0]), '', suf[1:], d)
    elif not suf:
        if v == int(pre):
            d[(v, pre, suf)] = True
        else:
            d[(v, pre, suf)] = False
    else:
        d[(v, pre, suf)] = (v == int(pre) + int(suf)) or bate(v, pre+suf[0], suf[1:], d) or bate(v-int(pre), suf[0], suf[1:], d)
    return d[(v, pre, suf)]

for num in numeros:
    d = dict()
    if bate(v, '', num, d):
        print(num)