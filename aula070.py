# return functions values

"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    print('Olha')
    print('só')
    print('que')
    print('legal')

    if x > 10:
        return 10
    return x + y
    print('Esse código é inalcançável')


variavel = print('David')  # Não retorna um valor

print(variavel is None)

variavel_2 = int('1')  # Retorna um valor
print(variavel_2)

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)
