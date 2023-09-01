# enumerate() and iterables

"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'David']
lista.append('João')

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)


for item in enumerate(lista):
    indice, nome = item
    print(indice)

for indices, nomes in enumerate(lista):
    print(indices, nomes)

for tupla_enumerada in enumerate(lista):
    for valor in tupla_enumerada:
        print(valor)
