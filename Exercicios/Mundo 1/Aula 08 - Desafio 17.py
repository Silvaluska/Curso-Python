'''
Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo. Calcule e mostre o comprimento da hipotenusa.
'''
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digote o valor do cateto adjascente: '))
from math import hypot
h = hypot(co, ca)
print('A hipotenusa do triangulo retangulo é {:.2f}'.format(h))