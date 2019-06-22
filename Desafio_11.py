#Calculo do Aumento de 15% sobre o salário do fucionário
salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print('O funcionário que recebia R${:.2f}, com 15% de aumento,  passou a receber R${:.2f}.'.format(salario, aumento))