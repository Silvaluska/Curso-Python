'''
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''
from desafio109 import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moeda.moeda(p)} é R$ {moeda.metade(p, True)}')
print(f'o dobro de R$ {moeda.moeda(p)} é R$ {moeda.dobro(p, True)}')
print(f'Aumentando 10% temos R$ {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13% temos R$ {moeda.diminuir(p, 13, True)}')