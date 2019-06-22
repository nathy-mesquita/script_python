#Aluguel de Carros
nome = input('Nome: ')
dias = int(input('Quantos dias permaneceu com o carro? '))
km = float(input('Quantos quilômetros foi rodado? '))
#R$60 por dia e R$0,15 por km
valor = (dias * 60) + (km * 0.15)
print('Sr(a). {}, o valor do aluguel seu carro é R${:.2f}'.format(nome, valor))