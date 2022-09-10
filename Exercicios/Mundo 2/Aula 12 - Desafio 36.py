'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não
pode exceder 30% do salário ou então o empréstimo será negado.'''
casa = float(input('Digite o valor da casa: R$'))
sala = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Em quantos anos pretende pagar essa casa: '))
parc = casa/(anos*12)
if parc > sala * 0.3:
    print('\033[31mSeu emprestimo foi negado, pois ultrapassou 30% do valor do seu salário')
    print('Salário = R${}'.format(sala))
    print('30% salário = R${:.2f}'.format(sala * 0.3))
    print('Parcela = R${:.2f}'.format(parc))
else:
    print('\033[32mSeu emprestimo foi aprovado!!')
    print('Sua parcela é de R${:.2f} e deve ser paga em {} anos'.format(parc, anos))