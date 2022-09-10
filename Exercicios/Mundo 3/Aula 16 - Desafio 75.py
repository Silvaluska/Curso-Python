'''
Exercício Python 075: Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.
'''
t = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))
print(f'O número 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O número 3 apareceu pela primeira vez na {t.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os números pares são: ', end='')
for c in t:
    if c%2 == 0:
        print(c,end=' ')