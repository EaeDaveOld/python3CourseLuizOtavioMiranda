# Dict manipulation

# Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome_completo'

pessoa[chave] = 'David Rodrigues'
pessoa['sobrenome'] = 'Silva'
print(pessoa[chave], pessoa['sobrenome'])

lista = []

pessoa[chave] = 'Walace Rodrigues'

del pessoa['sobrenome']

print(pessoa)

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print('EXISTE')
