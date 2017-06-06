__author__ = 'xyax'
import random
import string

N = int(raw_input('Numero de digitos: '))
print '1 -> Apenas numeros'
print '2 -> Numeros e letras'
print '3 -> Caracteres'
print
T = int(raw_input('Introduza a sua opcao: '))
r = str()
if T == 1:
    for i in xrange(N):
        r += str(random.randint(0, 9))
elif T == 2:
    for i in xrange(N):
        r += random.choice(string.ascii_letters + string.digits)
elif T == 3:
    for i in xrange(N):
        r += chr(random.choice(xrange(33, 126)))

print r