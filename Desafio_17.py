#Cálculo do Seno, Cosseno e Tangente
from math import radians, sin, cos, tan
num = float (input (' Insira o valor do ângulo: '))
sen = sin(radians(num))
print ('O Seno do ângulo {} é {:.2f}'.format(num, sen))
cos = cos(radians(num))
print ('O Cosseno do ângulo {} é {:.2f}'.format(num,cos))
tan = tan(radians(num))
print ('A Tangente do ângulo {} é {:.2f}'.format(num, tan))