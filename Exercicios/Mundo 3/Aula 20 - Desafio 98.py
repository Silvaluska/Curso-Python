'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
    a) de 1 até 10, de 1 em 1
    b) de 10 até 0, de 2 em 2
    c) uma contagem personalizada
'''
from time import sleep
def contador(inicio, fim, passo):
    passo = abs(passo)
    if passo == 0:
        passo = 1
    print('-='*30)
    print(f'Contage de {inicio} até {fim} pulande de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('Fim')
    else:
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ')
            sleep(0.5)
        print('Fim')


contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)