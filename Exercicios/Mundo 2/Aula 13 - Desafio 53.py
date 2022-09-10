'''Exercício Python 53: Crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo, desconsiderando os espaços.'''
f = input('Digite uma frase: ').strip().lower().replace(' ','')
inf = f[::-1]
if f == inf:
    print('Está frase é um palindromo')
else:
    print('Está frase não é um palindromo')