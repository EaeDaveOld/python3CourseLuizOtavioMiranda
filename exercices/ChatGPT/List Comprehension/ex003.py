# 3 - Dada uma lista de palavras, crie uma nova lista contendo o tamanho de cada palavra.
lista_palavras = ['Maça', 'David', 'Amor', 'Anel']
print(lista_palavras)

print()

nova_lista = [len(palavra) for palavra in lista_palavras]
print(nova_lista)
