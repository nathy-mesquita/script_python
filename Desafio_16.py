#cálculo da Hipotenusa a^2 = b^2 + c^2 - PITÁGORAS
from math import hypot
x = int(input("Cateto Oposto: "))
y = int(input('Cateto Adjacente: '))
print(hypot(x, y))