#quantos litros de tinta por metro quadrado
largura = float(input('Insira a largura do parede: '))
altura = float(input('Insira a Altura do parede: '))
area = largura * altura
l_tinta = area / 2
print('Sua parede é de {} X {} metros quadrados, e a sua área é {} m^2 '.format(largura, altura, area))
print('E para pintar essa parede, você precisará de {} litros de tinta por metro quadrado. '.format(l_tinta))