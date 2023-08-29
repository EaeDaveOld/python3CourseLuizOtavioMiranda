# Lists[] introduction
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(type(lista))
#         0    1          2             3    4
#        -5   -4         -3            -2   -1
# Os itens na lista, representa índices únicos.
lista = [123, True, 'David Rodrigues', 1.2, []]
lista[-3] = 'Maria'  # "Maria" passa a se tornar o item do índice 2 ou -3 da lista
print(lista)
print(lista[2].upper(), type(lista[2]))
