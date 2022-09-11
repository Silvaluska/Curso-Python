def leiaDinheiro(msg):
    n = input(msg)
    t = n.replace(',','')
    while True:
        if t.isnumeric() == True:
            return float(n.replace(',','.'))
        else:
            print(f'\033[41mERRO! "{n}" é um preço inválido\033[m')
            n = input(msg)