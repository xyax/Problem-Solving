__author__ = 'xyax'
import sys

linha = raw_input()
print('\n'.join(linha.split()))

'''
pals = list()
for line in sys.stdin:
    pals.append(line.rstrip('\n'))

print pals
pals.sort(key=len, reverse=True)
print(pals)'''