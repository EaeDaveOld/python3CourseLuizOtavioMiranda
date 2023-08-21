# Introduction to try/except

"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# print(1234)
# print(5678)
# int('a')  # -> Exception | ins't possible convert a to int

print('Será dobrado o número que você digitar.')
numero_str = input('Digite um número: ')

# if numero_str.isdigit():  # numero_str é número? (Somente números, não pontos)
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2}')
# else:
#     print('Isso não é um erro')  # O erro pode acontecer se o user
#     # digitar 1.5 por exemplo, o "." causaria o erro.

try:  # Tente fazer:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é o {numero_float * 2:.2f}')
    print('FLOAT', numero_float)
except:  # Se ocorrer um erro, então:
    print('Isso não é um número')
