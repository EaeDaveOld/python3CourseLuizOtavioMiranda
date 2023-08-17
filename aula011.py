# Order of precedence

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5  # Aqui a ordem é:
# 1 + 1 + 5
# 2 + 5
# 7
print(f'O resultado da conta é = {conta_1}')