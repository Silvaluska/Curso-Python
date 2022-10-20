class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto ... {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    def extrato(self):
        print(f'O titular {self.titular} possui R$ {self.saldo} na conta')
    def deposita(self, valor):
        self.saldo += valor
    def saca(self, valor):
        self.saldo -= valor


class Data:
    def __init__(self, day, month, year) -> None:
        self.day = day
        self.month = month
        self.year = year
    def formatada(self):
        print(f'{self.day}/{self.month}/{self.year}')

conta = Conta(123, 'Lucas', 2000, 10000)
conta.saldo = 2500
conta.extrato()
d = Data(21,11,2007)
d.formatada()