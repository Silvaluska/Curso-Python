'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))
print('''Qual operação você quer realizar?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
op = int(input('Qual sua escolha? '))
while op != 5:
    if op == 1:
        print('{} + {} = {}'.format(num1, num2, num1+num2))
    elif op == 2:
        print('{} x {} = {}'.format(num1, num2, num1*num2))
    elif op == 3:
        if num1 > num2:
            print('O {} é maior que {}'.format(num1, num2))
        else:
            print('O número {} é maior que o {}'.format(num2,num1))
    elif op == 4:
        num1 = float(input('Número 1: '))
        num2 = float(input('Número 2: '))
    else:
        print('Opção invalida, digite novamente')
    print('-=' * 20)
    op = int(input('Escolha outra operação: '))
print('-=' * 20)
print('Encerrando...')
sleep(1)
print('O programa foi encerrado')