# Exercice with Functions

# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicação = multiplicacao(5, 5, 5)
print(multiplicação)

# Crie uma função se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def par_ou_impar(numero):
    if numero % 2 == 0:
        # print(f'O número {numero} é par')
        return f'O número {numero} é par'
    # print(f'O número {numero} é ímpar.')
    return f'O número {numero} é ímpar'


parouimpar = par_ou_impar(5)
print(parouimpar)
