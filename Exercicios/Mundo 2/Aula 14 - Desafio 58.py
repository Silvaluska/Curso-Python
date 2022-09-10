'''
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
print('-='*26)
print('Vou pensar em um número de 0 a 10, tente advinhar...')
print('-='*26)
from random import randint
from time import sleep
r = randint(0,10)
num = int(input('Qual número eu pensei? '))
palpites = 1
print('Processando...')
sleep(1)
while num != r:
    if num > r:
        print('MENOS, Você errou')
    else:
        print('MAIS, Você errou')
    num = int(input('Tente novamente: '))
    palpites += 1
    print('Processando...')
    sleep(1)
print('PARABÉNS, você acertou')
print('Foram necessários {} palpites para vencer'.format(palpites))