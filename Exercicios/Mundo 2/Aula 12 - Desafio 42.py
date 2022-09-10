'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
    – EQUILÁTERO: todos os lados iguais
    – ISÓSCELES: dois lados iguais, um diferente
    – ESCALENO: todos os lados diferentes'''
print('-='*12)
print('Analisador de triangulos')
print('-='*12)
r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))
if abs(r1-r3)<r2<r1+r3:
    print('Essas retas podem formar um triângulo!!')
    if r1 == r2 == r3:
        print('Esse triângulo é Equilatero!!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse triângulo é Isósceles')
    else:
        print('Esse triângulo é escaleno')
else:
    print('Essas retas não podem formar um triângulo')