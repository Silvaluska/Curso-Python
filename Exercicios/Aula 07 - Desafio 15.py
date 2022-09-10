'''
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por
dia e R$0,15 por Km rodado.
'''
km = int(input('Quantos km foram rodados peo carro: '))
dia = int(input('Quantos dias você ficou com o carro: '))
pagar = km*0.15 + dia*60
print('O valor total a ser pago pelo aluguel do carro é R$ {:.2f}'.format(pagar))