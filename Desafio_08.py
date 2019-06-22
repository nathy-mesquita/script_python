#Conversor de Moeda
valor = float(input('Insira a quantidade em reais: '))
d = valor * 0.2614037
#Cotação dia 22/06/2019 - $3,83
print ('O valor R${:.2f} convertido em dólares ${:.2f}'.format(valor, d))