'''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu.'''
print('-='*25)
print('Vou pensar em um número de 0 a 5, tente advinhar...')
print('-='*25)
from random import randint
from time import sleep
r = randint(0,5)
num = int(input('Qual número eu pensei? '))
print('Processando...')
sleep(1)
if num == r:
    print('Parabéns, vc acertou!!')
else:
    print('ERROU, eu pensei no número {} e não no {}'.format(r, num))