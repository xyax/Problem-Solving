__author__ = 'xyax'

#!/usr/bin/python
import math

def nextPrime():
    x= primos[-1]+2
    m= int(math.sqrt(x))
    for j in range(len(primos)):
        if(primos[j]>m):
            return x
        if(x%primos[j]==0):
            x+=2
            j=0

n = input()
primos = [2, 3, 5, 7]
i=0
while (n > 1):
    if ((n%primos[i])==0):
        print (primos[i])
        n = n / primos[i]
    else:
        k=int(math.sqrt(n))
        if(primos[i]>k):
            print (n)
            break
        i+=1
        if(i==len(primos)):
            primos.append(nextPrime())
