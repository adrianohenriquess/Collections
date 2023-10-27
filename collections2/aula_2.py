usuarios = {1,5,76,34,52,13,17}
print(len(usuarios))

usuarios.add(14)
print(len(usuarios))

usuarios = frozenset(usuarios)
print(usuarios)

meu_texto = "Bem vindo meu nome é Adriano eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
palavras_sem_repeticao = set(meu_texto.split())
print(palavras_sem_repeticao)