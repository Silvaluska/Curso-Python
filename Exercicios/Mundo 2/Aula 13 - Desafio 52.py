'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
from math import sqrt
n = int(input('Digite um número: '))
r = n
a = 0
while a == 0:
    div = r % sqrt(r)
    if div == 0:
        print('consegui')
        a = sqrt(r)
    else:
        r = r -1
while n%a != 0:
    a = a - 1
if a == 1:
    print('Esse número é primo')
else:
    print('Esse número não é primo')