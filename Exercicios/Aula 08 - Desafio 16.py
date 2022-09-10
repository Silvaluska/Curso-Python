'''
Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''
from math import trunc
n = float(input('Digite um número real: '))
i = trunc(n)
print('O número {} tem a parte inteira {}'.format(n, i))