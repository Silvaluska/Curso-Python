'''
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em
uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
lista = []
for c in range(0,5):
    v = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(v)
        print('O valor foi adicionado no inicio da lista...')
    if v > max(lista):
        lista.append(v)
        print('O valor foi adicionado no final da lista...')
    for a in lista:
        if v < a:
            lista.insert(lista.index(a),v)
            print(f'O valor foi adicionado na posição {lista.index(a)} da lista...')
            break
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')