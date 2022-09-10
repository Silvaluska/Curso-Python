'''
Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
'''
ang = int(input('Digite um valor de angulo: '))
import math
angrad = math.radians(ang)
sen = math.sin(angrad)
cos = math.cos(angrad)
tan = math.tan(angrad)
print('O seno do angulo {} é {:.2f} \nO cosseno é {:.2f} \nA tangente é {:.2f}'.format(ang, sen, cos, tan))