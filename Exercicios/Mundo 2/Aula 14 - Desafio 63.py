'''
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8
'''
n = int(input('Quantos elementos da sequência de fibonacci você quer ver? '))
f1 = 0
f2 = 1
print('{} → {} → '.format(f1, f2), end='')
while n-2 != 0:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    n -= 1
    print('{}'.format(f3), end='')
    print(' → ' if n-2 != 0 else '', end='')
print('\nA Sequência acabou')
