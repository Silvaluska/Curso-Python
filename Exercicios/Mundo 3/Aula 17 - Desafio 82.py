'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
mostre o conteúdo das três listas geradas.
'''
lista1 = []
lista2 = []
lista3 = []
while True:
    lista1.append(int(input('Digite um valor: ')))
    r = input('Quer continuar S/N: ').strip().upper()
    if r == 'N':
        break
for a in lista1:
    if a%2 == 0:
        lista2.append(a)
    else:
        lista3.append(a)
print('9='*25)
print(f'A lista completa é {lista1}')
print(f'A lista de números pares é {lista2}')
print(f'A lista de números impares é {lista3}')