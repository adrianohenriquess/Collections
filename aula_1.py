idades = [39,30,27,18]

print(type(idades))
print(len(idades))
print(idades[2])

#adiciona no final da lista
idades.append(15)
print(idades)

#iterar em uma lista
for idade in idades:
    print(idade)

#idades.clear()
#print(idades)

if 15 in idades:
    idades.remove(15)

idades.insert(0, 20)
print(idades)

#inserir dois elementos na lista
idades.extend([23, 55])
print("Idades:")
print(idades)

idades_ano_que_vem = []
for idade in idades:
    idades_ano_que_vem.append(idade + 1)

print("Idades ano que vem:")
print(idades_ano_que_vem)

#Outra forma de somar um na lista
idades_ano_que_vem_2 = [(idade+1) for idade in idades]
print("Adicionando 1 as idades da lista de outra forma:")
print(idades_ano_que_vem_2)

#forma de filtrar os valores de uma lista em apenas uma linha
print("Filtrar idades")
print([idade for idade in idades if idade > 27])



def faz_processamento_de_visualizacao(lista = None):
  if lista == None:
     lista = list()
  print(len(lista))
  print(lista)
  lista.append(13)

idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)
print(idades)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

