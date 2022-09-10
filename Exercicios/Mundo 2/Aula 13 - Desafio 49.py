'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.'''
n = int(input('Digite um número: '))
print('A tabuada do {} é:'.format(n))
print('*'*12)
for c in range(1,11):
    t = n * c
    print('{} x {:2} = {}'.format(n, c, t))
print('*'*12)