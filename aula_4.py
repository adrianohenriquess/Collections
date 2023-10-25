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


class ContaMultiploSalario(ContaSalario):
    pass

conta1 = ContaSalario(1)
print(conta1)

conta2 = ContaSalario(2)
print(conta2)
print(conta1 == conta2)

#verificar se um objeto é uma instancia de um tipo especifico
print(isinstance(conta2, ContaSalario))