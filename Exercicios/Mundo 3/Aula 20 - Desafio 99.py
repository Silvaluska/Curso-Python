'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep
def maior(lista):
    print('-='*25)
    print('Analisando os valores passados...')
    for c in lista:
        print(c, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(lista)} valores ao todo')
    print(f'O maior valor informado foi {max(lista)}')


ln1 = [2, 9, 4, 5, 7, 1]
maior(ln1)
ln2 = [4, 7, 0]
maior(ln2)
ln3 = [1, 2]
maior(ln3)
ln4 = [6]
maior(ln4)