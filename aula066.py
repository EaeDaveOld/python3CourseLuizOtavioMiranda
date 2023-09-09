# Positional and Named Arguments def soma(x, y):

"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Argumentos posicionais


def soma(x, y, z):
    # Definição
    print(f'{x=} {y=} {z=} | x + y + z = {x + y + z}')


# print(soma(1, 2))
soma(1, 2, 3)
soma(y=2, z=3, x=1)

# Depois de passar um argumento nomeado, não é possível usar um argumento posicional
# soma(1, y=3, 3)

soma(1, y=2, z=3)
