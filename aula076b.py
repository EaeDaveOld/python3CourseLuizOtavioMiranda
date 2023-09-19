# Important dict methods

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

pessoa = {
    'nome': 'David Rodrigues',
    'sobrenome': 'Silva',
    'idade': 21,
}

pessoa.setdefault('endereço', 'test')

print(pessoa.__len__())  # Esse método retorna a quantidade de chaves

print(pessoa.keys())  # Esse método retorna as chaves

print(pessoa.values())  # Esse método retorna os valores

print(pessoa.items())  # Esse método retorna as chaves e os valores

print(pessoa['endereço'])

for chave in pessoa:  # Será iterado as chaves no dicionário
    print(chave)

for valor in pessoa.values():  # Será iterado os valores no dicionário
    print(valor)
