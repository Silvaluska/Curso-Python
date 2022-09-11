'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente.
'''
lista = []
while True:
    v = int(input('Digite um valor: '))
    while v in lista:
        print('Valor duplicado! não vou adicionar')
        v = int(input('Digite um valor: '))
    lista.append(v)
    print('Valor adicionado com sucesso!')
    c = input('Quer continuar S/N? ').upper()
    if c == 'N':
        break
print('*'*25)
lista.sort()
print(f'Você digitou os valores {lista}')