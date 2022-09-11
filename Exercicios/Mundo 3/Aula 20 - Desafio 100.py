'''
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
import random
from time import sleep
lista = []
def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for n in range(0,5):
        r = random.randint(0,10)
        print(r, end=', ')
        sleep(0.5)
        lista.append(r)
    print('Fim!')


sorteia()
def somaPar():
    s = 0
    print(f'Somando os valores pares da lista {lista}:', end=' ')
    for c in lista:
        if c%2 == 0:
            s += c
    print(f'Temos {s}')


somaPar()