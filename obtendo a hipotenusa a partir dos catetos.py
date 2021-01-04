import math

a = float(input('digite o valor de um dos catetos  '))
b = float(input('digite o valor do outro cateto  '))

A = pow(a, 2)
B = pow(b, 2)

C = math.sqrt(A)
D = math.sqrt(B)

E = C + D

print('a hipotenusa do triangulo retangulo cujo os catetos são {:.0f} e {:.0f}, é {:.0f}'.format(a, b, E))
