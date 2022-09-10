'''
Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
'''
n = int(input('Digite um número: '))
print('O antecessor de {} é {} e o sucessor é {}'.format(n, n-1, n+1))