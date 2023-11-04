meu_texto = "Bem vindo meu nome é Adriano eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
palavras_sem_repeticao = set(meu_texto.split())
print(palavras_sem_repeticao)

aparicoes = {
    "Guilherme": 1,
    "cachorro" : 2,
    "nome"     : 2,
    "vindo"    : 1,
}

print(type(aparicoes))
print(aparicoes["Guilherme"])
print(aparicoes["cachorro"])
#caso não exista, mostra 0
print(aparicoes.get("rewqrwq", 0))

aparicoes = dict(Guilherme = 2, cachorro = 1)
print(aparicoes)

aparicoes = {
    "Guilherme": 1,
    "cachorro" : 2,
    "nome"     : 2,
    "vindo"    : 1,
}

aparicoes["Carlos"] = 1
print(aparicoes)
aparicoes["Carlos"] = 2
print(aparicoes)

#apagar um elemento
del aparicoes["Carlos"]
print(aparicoes)

print("cachorro" in aparicoes)

#iterar
for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

print("Values")
for elemento in aparicoes.values():
    print(elemento)

print("chave e valor")
for elemento in aparicoes.keys():
    print(elemento, aparicoes[elemento])

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, "=", valor)

palavras = ["palavra {}".format(chave) for chave in aparicoes.keys()]
print(palavras)