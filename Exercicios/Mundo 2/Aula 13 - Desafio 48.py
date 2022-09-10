'''Exercício Python 48: Faça um programa que calcule a soma entre todos os números
que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
s = 0
qtd = 0
for c in range(1,501):
    if c%2 != 0 and c%3 == 0:
        s += c
        qtd += 1
print('A somda de todos os {} números impares que são multiplos de 3 é {}'.format(qtd, s))