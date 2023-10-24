class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {} <<]".format(self.codigo, self.saldo)


conta = ContaCorrente(15)
print(conta)
conta.deposita(500)
print(conta)

conta2 = ContaCorrente(47685)
conta2.deposita(1000)
print(conta2)

contas = [conta, conta2]
print(contas)
#for conta in contas:
 #   print(conta)
# mesma referencia do objeto na lista
#contas = [conta, conta2, conta]
#print(contas[0])
#conta.deposita(1000)
#print(contas[0])
#print(contas[2])

#############################################################
contas_2 = [conta, conta2]
def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

deposita_para_todas(contas_2)
for conta in contas:
    print(conta)

contas_2.insert(0, 76)
print(contas_2[0], contas_2[1], contas_2[2])

#tuplas representação imutavel
adriano = ('Adriano', 35, 1988)
camila  = ('Camila', 34, 1989)
print(adriano[0])
print(camila[2])

usuarios = [adriano, camila]
print(usuarios)
usuarios.append(('Paulo', 43, 1975))
print(usuarios)

