'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
jogador = {}
jogador['Nome'] = input('Nome: ')
p = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
gols = []
for c in range(p):
    gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
jogador['Gols'] = gols
jogador['Total de gols'] = sum(gols)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} fez {p} gols')
for i,g in enumerate(jogador['Gols']):
    print(f'    => Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {jogador["Total de gols"]}')