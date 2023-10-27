usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = []

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

conjunto = set(assistiram)
print(conjunto)

##criar um conjunto
conjunto2 = set([1,2,3,1])
print(conjunto2)
print(type(conjunto2))

for usuario in conjunto:
    print(usuario)

#união dos dois conjuntos
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
print(usuarios_machine_learning | usuarios_data_science)

#intesecção dos dois conjuntos
print(usuarios_machine_learning & usuarios_data_science)

#retirando itens que ja apareceram no primeiro conjunto
print(usuarios_data_science - usuarios_machine_learning)
fez_data_science_mas_nao_machine_learning = usuarios_data_science - usuarios_machine_learning
print(15 in fez_data_science_mas_nao_machine_learning)
print(23 in fez_data_science_mas_nao_machine_learning)

#extrair o conjunto ou exclusivo entre os dois
#pessoas que aparecem nos dois conjuntos, mas só em um deles por vez
conjunto_pessoas_que_aparecem_nos_dois_mas_so_em_um_deles = usuarios_machine_learning ^ usuarios_data_science
print(conjunto_pessoas_que_aparecem_nos_dois_mas_so_em_um_deles)
