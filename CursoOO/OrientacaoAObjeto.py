class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O titular {self.__titular} possui R$ {self.__saldo} na conta')

    def depositar(self, valor):
        self.__saldo += valor

    def __limite_saque(self, valor):
        return valor <= (self.__saldo + self.__limite)

    def sacar(self, valor):
        if self.__limite_saque(valor):
            self.__saldo -= valor
        else:
            print(f'Seu limite de saque é apenas {self.__saldo + self.__limite}')

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return '001'


class Data:
    def __init__(self, day, month, year) -> None:
        self.__day = day
        self.__month = month
        self.__year = year
    def formatada(self):
        print(f'{self.__day}/{self.__month}/{self.__year}')

lista = []
for i in range(10):
    lista[i] = Conta(123, 'lucas', 2000, 100)