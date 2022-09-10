'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
n = int(input('Digite um número: '))
a = n - 1
res = 0
for r in range(a,1,-1):
    if n%r == 0:
        res = 1
if res == 1:
    print('Esse número não é primo')
else:
    print('Esse número é primo')