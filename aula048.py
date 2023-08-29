# Lists[] introduction
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
import os
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

os.system('cls')  # Nesse estágio do programa, o terminal será limpado

lista_2 = [10, 20, 30, 40]  # Foi criado uma lista com os itens 10, 20, 30 e 40
print(f'Aqui é a lista completa = {lista_2}')

numero = lista_2[2]  # Uma variável numero recebeu o valor do índice 2, 30

del lista_2[2]  # Foi deletado o item do índice 2 (30)
print(f'Aqui é a lista com o índice 2 deletado = {lista_2}')

# O índice 2 passou a ser 40, que era o último item da lista
print(f'Aqui é o novo índice 2 = {lista_2[2]}')
lista_2.append(30)  # Foi adicionado o item 30 na lista, na última posição
print(f'Foi adicionado o item {lista_2[3]} na lista {lista_2}')

lista_2.pop()  # Remove o último item da lista
print(f'Foi removido o último item da lista = {lista_2}')

ultimo_valor = lista_2.pop()
print(ultimo_valor)
