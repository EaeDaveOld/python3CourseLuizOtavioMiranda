# copy, sorted, produtos.sort
# Exercícios
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print('PRODUTOS ORIGINAIS')
print(f'{produtos}\n\n')


# Aumente os preços dos produtos 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = produtos.copy()
index = 0
for produto in produtos:
    novos_produtos[index]['preco'] = novos_produtos[index]['preco'] + \
        (novos_produtos[index]['preco'] * 0.10)
    index += 1

print("NOVOS_PRODUTOS - 10% MAIS CAROS")
print(f'{novos_produtos}\n\n')


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
print("PRODUTOS_ORDENADOS_POR_NOME - DECRESCENTE")
produtos_ordenados_por_nome = sorted(
    novos_produtos.copy(), key=lambda x: x['nome'], reverse=True)
print(f'{produtos_ordenados_por_nome}\n\n')


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
print("PRODUTOS_ORDENADOS_POR_PRECO - CRESCENTE")
produtos_ordenados_por_preco = sorted(
    produtos_ordenados_por_nome.copy(), key=lambda x: x['preco'])
print(f'{produtos_ordenados_por_preco}\n\n')
