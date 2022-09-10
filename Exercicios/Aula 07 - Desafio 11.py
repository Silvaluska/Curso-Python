'''
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''
a = float(input('Digite a altura da sua parede: '))
l = float(input('Digite a largura da sua parede: '))
print('Sua parede possui {:.2f} m² e são necessários {:.2f} litros de tinta para pinta-la'.format(a*l, (a*l)/2))