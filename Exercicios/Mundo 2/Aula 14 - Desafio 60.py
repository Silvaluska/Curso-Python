'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
'''
num = f = int(input('Digite um número: '))
r = 1
print('Calculando o fatorial de {}! = '.format(num), end='')
while f != 0:
    r *= f
    print('{}'.format(f), end='')
    print(' x ' if f != 1 else ' = ', end='')
    f -= 1
print('{}'.format(r))