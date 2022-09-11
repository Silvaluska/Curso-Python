'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
maior número no dado.
'''
from random import randint
from time import sleep
joga = {}
for c in range(0,4):
    joga[f'Jogador {c+1}'] = randint(0,10)
    print(f'O Jogador {c+1} tirou {joga[f"Jogador {c+1}"]}')
    sleep(0.5)
print('-='*20)
print(f'{"Ranking dos Jogadores":^30}')
cont = 1
for i in sorted(joga, key=joga.get, reverse=True):
    print(f'    - O {cont}ª Lugar: {i} com {joga[i]}')
    sleep(.5)
    cont += 1