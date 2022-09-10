'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.'''
me = float(input('Digite seu peso: '))
ma = me
for c in range(0,4):
    p = float(input('Digite seu peso: '))
    if p > ma:
        ma = p
    elif p < me:
        me = p
print('O maior peso é {} e o menor peso é {}'.format(ma, me))