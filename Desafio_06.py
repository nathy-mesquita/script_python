#Conversor de Medidas
m = float(input('Digite uma media em metros: '))
#Decâmetro
dam = m / 10
#Hectômetro
hm = m / 100
#Quilômetro
km = m / 1000
#Decimetro
dm = m * 10
#Centimetro
cm = m * 100
#Milimetro
mm = m * 1000
print('O valor {} em Metros corresponde a: \n{} Milimetros. \n{} Centimentros. \n{} Decimentros.'.format(m,mm,cm,dm), end='')
print('\n{} Decâmetros. \n{} Hectômetros. \n{} Quilômetros.'.format(dam, hm, km))