'''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se
ele quer ou não continuar a digitar valores.
'''
n = me = s = int(input('Digite um número: '))
ma = 0
qtd = 1
c = input('Você quer continuar S/N: ').upper()
while c == 'S':
    n = int(input('Digite um número: '))
    s += n
    qtd += 1
    if n > ma:
        ma = n
    elif n < me:
        me = n
    c = input('Você quer continuar S/N: ').upper()
print('A média dos números digitados é {:.2f}'.format(s/qtd))
print('O maior número é {}'.format(ma))
print('O menor número é {}'.format(me))