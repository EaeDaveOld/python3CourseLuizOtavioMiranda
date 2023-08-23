# id object value - unique memory value identifier

"""
Flag (Bandiera) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

v1 = 'a'  # A variável v1 recebe o valor 'a', e possui um ID na memória
v2 = 'a'  # O Python identifica que ambas possuem o mesmo valor na memória e reutiliza

# Assim, os IDs são iguais:
print(f'{id(v1)}\n{id((v2))}')

# o id é o identificar do objeto na memória
# condicao = False


# if condicao:
#   print('Faça algo')
# else:
#   Print('Não faça algo')