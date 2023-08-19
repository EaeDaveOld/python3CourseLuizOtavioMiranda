# in and not in Operator - Iterability
# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4
#  D a v i d
# -5-4-3-2-1

nome = 'David'
print(f'Aqui está o 2° índice da string "{nome}" = {nome[2]}')

print('D' in nome)  # A letra "D" está entre "David" -> True

# A string "Matheus" não está entre "David" -> True
print('Matheus' not in nome)
