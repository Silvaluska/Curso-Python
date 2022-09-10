'''
Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
m = float(input("Digite o valor em metros: "))
print('O valor em cm é {:.0f} \nO valor em mm é {:.0f}'.format(m*100, m*1000))