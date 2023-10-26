from operator import attrgetter
from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo  = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Código {} Saldo {} <<]".format(self._codigo, self._saldo)

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo

    #outra forma com less than
    #se os saldos forem diferentes compara o saldo
    #senao compara os codigos
    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo



conta_do_guilherme = ContaSalario(48)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(56)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(5)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_do_paulo, conta_da_daniela]
#ordenar pelo saldo e acrescentar o criterio de desempate
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)

print()

conta_do_guilherme = ContaSalario(48)
conta_do_guilherme.deposita(12)

conta_da_daniela = ContaSalario(56)
conta_da_daniela.deposita(1200)

conta_do_paulo = ContaSalario(5)
conta_do_paulo.deposita(1199)
contas = [conta_do_guilherme, conta_do_paulo, conta_da_daniela]
#ordenar pelo saldo e acrescentar o criterio de desempate
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)

print("Usando o criterio de ordenação definido no lt para ordenar")
for conta in sorted(contas):
    print(conta)

#usando o decorator total ordering para verificar todas as comparações possíveis
print(conta_do_guilherme <= conta_da_daniela)
print(conta_do_guilherme >= conta_da_daniela)
print(conta_do_guilherme <= conta_do_guilherme)
