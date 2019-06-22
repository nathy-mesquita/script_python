#Desconto de 5% de Desconto
preco = float(input('Preço do Produto: R$'))
des = preco - (preco * (5/100))
print('O produto que custa R${:.2f},  a vista com 5% de desconto sai por R${:.2f}.'.format(preco, des))