__author__ = 'xyax'
pal = 'abcd'
#pale = enumerate(pal)
#print pale
#for i, letter in pale:
#    print i, letter

def vamosVer(w):
    if len(w) == 1:
        yield w
    for i in range(len(w)):
        yield w[:i]

lw = list(vamosVer(pal))
for l in lw:
    print l