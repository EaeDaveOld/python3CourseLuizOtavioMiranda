# Format interpolation %

"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
"""

nome = 'David'
preco = 1000.95897643

# Formatação de strings utilizando o método de interpolação com %
variavel = '%s, o preço total é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %i é %X' % (500, 500))
