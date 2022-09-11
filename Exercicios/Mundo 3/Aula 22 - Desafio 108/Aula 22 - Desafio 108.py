'''
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional
chamada moeda() que consiga mostrar os números como um valor monetário formatado.
'''
from desafio108 import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moeda.moeda(p)} é R$ {moeda.moeda(moeda.metade(p))}')
print(f'o dobro de R$ {moeda.moeda(p)} é R$ {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% temos R$ {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13% temos R$ {moeda.moeda(moeda.diminuir(p, 13))}')