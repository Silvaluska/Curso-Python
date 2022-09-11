'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em
ordem crescente.
'''
num = [[], []]
for n in range(0,7):
    r = int(input('Digite o número: '))
    if r%2 == 0:
        num[0].append(r)
    else:
        num[1].append(r)
num[0].sort()
num[1].sort()
print('-='*30)
print(f'Os valores pares são {num[0]}')
print(f'Os números impares são {num[1]}')