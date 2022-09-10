'''Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.'''
print('-='*12)
print('Analisador de triangulos')
print('-='*12)
r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))
if abs(r1-r3)<r2<r1+r3:
    print('Essas retas podem formar um triangulo!!')
else:
    print('Essas retas não podem formar um triangulo')