# len Function and slice string

"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""

variavel = 'Olá mundo'

# Vai ser omitido tudo antes do 4° index da variavel e impresso tudo depois
print(variavel[4:])

# Vai ser omitido tudo antes do 4° index da variavel e impresso até o 5° index
print(variavel[4:6])

data_nascimento = '28/11/2001'

print(data_nascimento[3:5])  # Imprimirá somente o mês
print(data_nascimento[6:])  # Imprimirá somente o ano
print(data_nascimento[-10:-8])  # Imprimirá somente o dia

# A função len retorna a quantidade de caracteres
print(
    f'Nesta string {data_nascimento = } contém {len(data_nascimento)} caracteres totais')

# Desta forma estará pulando 2 index a cada leitura
print(data_nascimento[0:10:2])
# 0123456789
# 28/11/2021
# -10987654321

# Desta forma está invertido, de trás pra frente
print(f'Test {data_nascimento[::-1]}')
