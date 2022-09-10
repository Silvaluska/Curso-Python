'''
Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça
um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
aln1 = input('Digite o nome do primeiro aluno: ')
aln2 = input('Digite o nome do segundo aluno: ')
aln3 = input('Digite o nome do terceiro aluno: ')
aln4 = input('Digite o nome do Quarto aluno: ')
from random import shuffle
seq = [aln1, aln2, aln3, aln4]
shuffle(seq)
print('A sequencia de apresentação é {}'.format(seq))