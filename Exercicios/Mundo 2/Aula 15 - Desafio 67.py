'''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
n = t = 0
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    print('A tabuada do {} é:'.format(n))
    print('*' * 12)
    for c in range(1, 11):
        t = n * c
        print('{} x {:2} = {}'.format(n, c, t))
    print('*'*12)
print('Programa tabuada encerrado')