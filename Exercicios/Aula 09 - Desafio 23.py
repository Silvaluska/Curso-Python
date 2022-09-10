'''
Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''
num = int(input('Digite um numero de 0 a 9999: '))
u = num % 10
d = num // 10 %10
c = num // 100 % 10
m = num // 1000
print('Milhar: {}'.format(m))
print('Centenas: {}'.format(c))
print('Dezenas: {}'.format(d))
print('Unidade: {}'.format(u))