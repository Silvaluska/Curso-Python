'''Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
parta viagens mais longas.'''
km = int(input('Digite a distância da viagem em Km: '))
if km > 200:
    v = km * 0.45
    print('O preço da passagem é R$ {}'.format(v))
else:
    v = km * 0.5
    print('O preço da passagem é R$ {}'.format(v))