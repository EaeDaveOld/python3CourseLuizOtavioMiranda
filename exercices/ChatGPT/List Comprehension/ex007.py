# 7 - Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam com a letra "A".
nomes = ['David', 'Alana', 'Marcos', 'Alex', 'Joana']

nomes_A = [nome for nome in nomes if nome.startswith('A')]
print(nomes_A)
