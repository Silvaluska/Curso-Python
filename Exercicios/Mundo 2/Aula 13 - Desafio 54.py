'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
a = date.today().year
ma = 0
me = 0
for c in range(0,7):
    i = int(input('Digite a sua idade: '))
    if (a - i) < 21:
        me += 1
    elif (a - i) >= 21:
        ma += 1
print('Desse grupo {} pessoas atigiram a maioridade e {} pessoas ainda são menores de idade'.format(ma, me))