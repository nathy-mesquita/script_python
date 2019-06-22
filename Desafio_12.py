#Conversor de Temperatura
c = float(input('Insira a temperatura em Celcius: '))
#Celcius p/ Kelvin
k = c + 273.15
#Celcius p/ Fahrenheit
f = ((9*c)/5)+32
print ('A temperatura {}°C corresponde {}°F e {} K.'.format(c,f,k))