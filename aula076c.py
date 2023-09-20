# Shallow Copy vs Deep Copy

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],  # Dado mutável
}

d2 = d1  # d2 está apontando o valor de d1

#
d2['c1'] = 30  # A chave c1 está recebendo o valor 30

print(d1['c1'])  # A chave c1 da lista d1 está com o valor 30

# Essa cópia é rasa pois se no dicionário possuir chaves
# que contem dados mutáveis (listas e outros dicionários)
# esses dados serão linkados e não copiados

d3 = d2.copy()  # d3 é a copia rasa de d2 atual

d4 = copy.deepcopy(d1)  # cópia profunda

d4['l1'][0] = 100
print(d1)
print(d4)


d3['c1'] = 100

print(d2['c1'])  # A chave c1 da lista d2 continua valendo 30

print(d3['c1'])  # A chave c1 da lista d3 vale 100
