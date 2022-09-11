'''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
print('-'*36, '\n{:^35}'.format('Listagem de preços'))
print('-'*36)
lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for c in range(0,len(lista),2):
     print(f'{lista[c]:.<26}', f'R$ {float(lista[c+1]):>6.2f}')
print('-'*36)