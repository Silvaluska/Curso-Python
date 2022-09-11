'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
lista = []
while True:
    jogador = {}
    jogador['Nome'] = input('Nome: ')
    p = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols = []
    for c in range(p):
        gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['Gols'] = gols
    jogador['Total de gols'] = sum(gols)
    lista.append(jogador.copy())
    r = input('Quer continuar S/N: ').upper()
    print('-'*30)
    if r == 'N':
        break
print(f'{"cod"}{"nome":^10}{"gols":^8}{"Total":^15}')
print('-'*35)
for i in lista:
    g = str(i['Gols'])
    print(f'{lista.index(i)}    {i["Nome"]:9}{g:15}{i["Total de gols"]}')
while True:
    r = int(input('Mostrar dados de Qual jogador? '))
    if r == 999:
        break
    print(f'Levantamento do jogador {lista[r]["Nome"]}')
    for i,g in enumerate(lista[r]["Gols"]):
        print(f'    => Na partida {i+1}, fez {g} gols.')
    print(f'    => Foi um total de {jogador["Total de gols"]}')