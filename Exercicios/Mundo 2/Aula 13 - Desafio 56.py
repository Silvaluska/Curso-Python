'''
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
from datetime import date
h = date.today().year
s = vnome = qtd = mv = 0
for c in range(1,5):
    print('-'*5,'{}ª pessoa'.format(c),'-'*5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M] mulher [H] homem: ').upper()
    s += idade
    if idade > mv and sexo == 'H':
        vnome = nome
        mv = idade
    if idade < 20 and sexo == 'M':
        qtd += 1
print('-'*12,' Analisando ', '-'*12)
print('A média de idade dessas pessoas é: {}'.format(s/4))
print('O Homem mais velho é {} e ele possui {} anos'.format(vnome, mv))
print('{} Mulheres estão abaixo de 20 anos'.format(qtd))