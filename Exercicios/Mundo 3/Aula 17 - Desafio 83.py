'''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu
aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
e = input('Digite a sua expressão: ')
lista = []
for c in e:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Sua expressão é valida')
else:
    print('Sua expressão é incorreta')