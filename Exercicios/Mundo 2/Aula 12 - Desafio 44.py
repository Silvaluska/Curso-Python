'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
    – à vista dinheiro/cheque: 10% de desconto
    – à vista no cartão: 5% de desconto
    – em até 2x no cartão: preço formal
    – 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format(' Lojas Silva '))
valor = float(input('Digite o valor do produto: R$'))
print('-='*20)
print('''Digite a condição de pagamento
Pagamento a vista dinheiro/cheque digite [0]
Pagamento a vista no cartão digite [1]
Pagamento em 2x no cartão digite [2]
Pagamento em 3x ou mais no cartão digite [3]''')
print('-='*20)
cond = int(input('Escolha sua forma de pagamento: '))
if cond == 0:
    print('O valor a ser pago é de R${:.2f}'.format(valor*0.9))
elif cond == 1:
    print('O valor a ser pago é de R${:.2f}'.format(valor * 0.95))
elif cond == 2:
    print('Sua compra será parcelada em 2 vezes de R${}'.format(valor/2))
    print('O valor a ser pago é de R${:.2f}'.format(valor))
elif cond == 3:
    parc = int(input('Quantas parcelas: '))
    print('Sua compra será parcelada em {} vezes de R${}'.format(parc, valor/parc*1.2))
    print('O valor a ser pago é de R${:.2f}'.format(valor * 1.2))
else:
    print('Você é burro pra cacete, digitou a condição de pagamento errada seu animal')