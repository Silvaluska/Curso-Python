'''
Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''
c = float(input('Digite a temperatura em celcius: '))
f = c*(9/5)+32
k = c+273.15
print("A temperatura de {:.2f}°C Corresponde a {:.2f}ºF e a {:.2f}ºK".format(c, f, k))