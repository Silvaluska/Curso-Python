''''
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
cont = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'Nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
s = int(input('Digite um número entre 0 e 20: '))
while s > 20 or s < 0:
    print('Tente novamente')
    s = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {cont[s]}')