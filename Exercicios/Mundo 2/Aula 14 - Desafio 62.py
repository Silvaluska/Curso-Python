'''
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
print('-='*20)
print('{:^40}'.format('10 Termos de uma PA'))
print('-='*20)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
c = 1
while c != 11:
    print(n, end=' → ')
    n += r
    c += 1
c = int(input('Quantos termos você quer ver a mais? '))
qtd = 10
while c != 0:
    for t in range(1, c+1):
        print(n, end=' → ')
        n += r
        qtd += 1
    c = int(input('Quantos termos você quer ver a mais? '))
print('A progessão foi finalizada com {} termos'.format(qtd))