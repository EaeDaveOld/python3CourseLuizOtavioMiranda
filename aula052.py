# tuple type - unchanging list

"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'David')  # Tuple
# nome[1] = 'Jorge'
print(nomes)
print(nomes[0])
print(nomes[-1])

nomes_list = ['David', 'Lucas', 'Caio']  # List

# nomes_tuple receive nomes_list convert into tuple
nomes_tuple = tuple(nomes_list)
print(nomes_tuple)
