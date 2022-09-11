'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = input('Quer continuar S/N: ').upper()
    if r == 'N':
        break
print('*'*30)
print(f'{len(lista)} números foram digitados')
lista.sort(reverse=True)
print(f'{lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista')
else:
    print('Não digitaram nenhum valor 5')