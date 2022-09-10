'''Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
v = int(input('Digite a velocidade do carro em km/h: '))
if v > 80:
    print('O carro ultrapassou a velocidade maxima da via')
    m = (v-80)*7
    print('A multa aplicada deve ser de R$ {}'.format(m))
else:
    print('O carro está dentro do limite permitido pela via')