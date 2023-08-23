# flags, id, is, is not, None
# id object value - unique memory value identifier
"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

v1 = 'a'  # A variável v1 recebe o valor 'a', e possui um ID na memória
v2 = 'a'  # O Python identifica que ambas possuem o mesmo valor na memória e reutiliza

# Assim, os IDs são iguais:
print(f'{id(v1)}\n{id((v2))}')
# o id é o identificar do objeto na memória

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True  # Essa variável só é criada, SE a "condicao" for TRUE
else:
    pass

if passou_no_if is None:
    print('Não passou no if')


if passou_no_if is not None:
    print('Passou no if')