import array as ar
from abc import abstractmethod, ABCMeta

import numpy as np
class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    @abstractmethod
    def passa_o_mes(self):
        pass

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {} <<]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.06
        self._saldo -= 1


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

conta18 = ContaInvestimento(18)
conta18.deposita(450)
conta18.passa_o_mes()

#lista de contas
contas = [conta16, conta17, conta18]
for conta in contas:
    conta.passa_o_mes()
    print(conta)

array = ar.array('d', [1, 3.5])
print(array)

numeros = np.array([1, 3.5])
print(numeros)
print(numeros + 3)