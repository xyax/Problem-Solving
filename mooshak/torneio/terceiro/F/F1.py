import sys

numeros = list()
v = int(raw_input())
for line in sys.stdin:
    numeros.append(line.rstrip('\n'))

def bate(v, pre, suf):
    if not pre:
        if not suf:
            return False
        elif v == int(suf):
            return True
        return bate(v, suf[0], suf[1:]) or bate(v-int(suf[0]), '', suf[1:])
    if not suf:
        if v == int(pre):
            return True
        return False
    return (v == int(pre) + int(suf)) or bate(v, pre+suf[0], suf[1:]) or bate(v-int(pre), suf[0], suf[1:])


for num in numeros:
    if bate(v, '', num):
        print(num)