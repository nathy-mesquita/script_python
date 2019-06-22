'''Dobro - Triplo - Raiz quadrada '''
n = float(input('digite um número: '))

#Dobro
d = n*2
#Triplo
t = n*3
#Raiz quadrada
r = pow(n, (1/2))
'''ou r = n ** (1/2)'''

print('Tendo o número {:.2f}, o dobro é: {:.2f}, o triplo é: {:.2f} e a raiz quadrada é: {:.2f}.' .format(n,d,t,r))