__author__ = 'xyax'

#preencher uma lista usando compreensao

def geraMatriz(x0, x1, y0, y1):
    m= [['0']*(x1-x0)]*(y1-y0)
    return m

xMin= yMin= 0
xMax=4
yMax=10

matriz= geraMatriz(xMin, xMax, yMin, yMax)
for l in matriz:
    print l