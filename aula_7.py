from operator import attrgetter
#ordenação sem ordem natural
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
    def __lt__(self, other):
        return self._saldo < other._saldo

conta_do_guilherme = ContaSalario(48)
conta_do_guilherme.deposita(500)

conta_da_dani = ContaSalario(56)
conta_da_dani.deposita(1000)

conta_do_paulo = ContaSalario(5)
conta_do_paulo.deposita(451)

contas = [conta_do_guilherme, conta_do_paulo, conta_da_dani]
for conta in contas:
    print(conta)

#ordenar contas
def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
    print(conta)

print()
# outra forma
for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

print(conta_do_guilherme < conta_da_dani)
for conta in sorted(contas):
    print(conta)

for conta in sorted(contas, reverse=True):
    print(conta)
