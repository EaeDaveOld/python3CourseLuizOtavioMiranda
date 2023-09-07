# Ternary Operator - One line condicional

"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

# condicao = 10 == 10
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)

digito = 9
novo_digito1 = digito if digito <= 9 else 0  # condição de uma só linha
novo_digito2 = 0 if digito > 9 else digito  # same as above
print(novo_digito1)
print(novo_digito2)
