# isinstance - para saber se o objeto é de determinado tipo
lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'David'}]

for valor in lista:
    if isinstance(valor, str):
        valor = valor.upper()
        print(f'O valor "{valor}" é do tipo "str"')

    if isinstance(valor, int):
        print(f'O valor "{valor}" é do tipo "int"')

    if isinstance(valor, float):
        print(f'O valor "{valor}" é do tipo "float"')

    if isinstance(valor, bool):
        print(f'O valor "{valor}" é do tipo "bool"')

    if isinstance(valor, list):
        print(f'O valor "{valor}" é do tipo "list"')

    if isinstance(valor, tuple):
        print(f'O valor "{valor}" é do tipo "tuple"')

    if isinstance(valor, set):
        print(f'O valor "{valor}" é do tipo "set"')

    if isinstance(valor, dict):
        print(f'O valor "{valor}" é do tipo "dict"')
