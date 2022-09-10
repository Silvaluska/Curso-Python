'''Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o térceiro número: '))
max = n1
min = n1
if n2 > max:
    max = n2
if n3 > max:
    max = n3
if n2 < min:
    min = n2
if n3 < min:
    min = n3
print('O valor máximo é {} e o minimo é {}'.format(max, min))