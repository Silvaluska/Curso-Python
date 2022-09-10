'''
Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela
pode comprar.
'''
r = float(input("Digete o valor em real que você tem na carteira: "))
print('Com {} reais você pode comprar {:.2f} dolares'.format(r, r/5.3))