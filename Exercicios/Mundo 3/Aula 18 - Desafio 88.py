'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.
'''
from random import sample
from time import sleep
print('-='*30)
print(f'{"Jogos da mega sena":^60}')
print('-='*30)
palpites = int(input('Quantos palpites você quer? '))
mega = []
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
         41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
         51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
for a in range(0,palpites):
    mega.append(sample(lista, 6))
print('-='*30)
print(' '*20, f'Sorteando {palpites} Jogos')
print('-='*30)
for a in range(0,len(mega)):
    mega[a].sort()
    print(f'O jogo {a+1}: {mega[a]}')
    sleep(1)
print('-='*11, '< Boa Sorte >', '-='*11)