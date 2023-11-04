from collections import defaultdict

meu_texto = "Bem vindo meu nome é Adriano eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = {}
for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

aparicoes_valor_padrao = defaultdict(int)
for palavra in meu_texto.split():
    ate_agora = aparicoes_valor_padrao[palavra]
    aparicoes_valor_padrao[palavra] = ate_agora + 1

print(aparicoes_valor_padrao)

from collections import Counter

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

#aparicoes = Counter()
#for palavra in meu_texto.split():
#  aparicoes[palavra] += 1

#print(aparicoes)

aparicoes = Counter(meu_texto.split())

print(aparicoes)