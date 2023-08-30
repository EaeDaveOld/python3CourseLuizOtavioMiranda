# list[] - extend method and concatenation
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# Foi concatenado as duas listas e armazenadas em uma variável
lista_c = lista_a + lista_b
print(lista_c)

# ista_a extende lista_b, ou seja, lista_a = [1, 2, 3, 4, 5, 6]
lista_a.extend(lista_b)  # Esse método modifica extendendo o objeto em si
print(lista_a)
