'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o
tempo que falta ou que passou do prazo.'''
from datetime import date
today = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = today - ano
if idade < 18:
    print('\033[31mVocê ainda não está na idade de se alistar\nAinda faltam {} anos para seu alistamento'.format(18-idade))
    print('Seu alistamento será no ano de {}'.format(today+(18-idade)))
elif idade == 18:
    print('\033[32mVocê possui 18 anos e está na idade para se alistar')
else:
    print('\033[31mVocê passou {} anos da idade de alistamento obrigatorio'.format(idade-18))
    print('Seu alistamento aconteceu no ano de {}'.format(today-(idade-18)))