# Exercice - show index from list

"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    indice = lista.index(nome)
    print(indice, nome)


lista_2 = ['Maria', 'Helena', 'Luiz']
lista_2.append('David')

indices = range(len(lista_2))

for indice in indices:
    print(indice, lista_2[indice])
