'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a
razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
print('-='*20)
print('{:^40}'.format('10 Termos de uma PA'))
print('-='*20)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
for c in range(0,10):
    print(n, end=' → ')
    n += r
print('Acabou')