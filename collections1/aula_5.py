idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])

print(list(range(len(idades))))

#usando enumerate
print(list(enumerate(idades)))

#desempacotar a tuplas geradas pelo enumerate
for indice, idade in enumerate(idades):
    print(indice, idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios: # ja desempacotando
    print(nome, idade, nascimento)

for nome, _, _ in usuarios:  # desempacotar so o nome e ignorar o resto
    print(nome)

## aula 6
#ordenando listas
print(sorted(idades))

#lista reversa
print(list(reversed(idades)))

#lista decrescente
print(sorted(idades, reverse=True))
#ou
print(list(reversed(sorted(idades))))
#ou ordernar a lista diretamente para mudar efetivamente a ordem dos seus valores
idades.sort()
print(idades)

