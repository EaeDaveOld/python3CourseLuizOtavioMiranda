# Exercice - Multiplier function using closure

# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicar(numero):
#     return f'O número "{numero}" DUPLICADO é = {float(numero) * 2}'


# def triplicar(numero):
#     return f'O número "{numero}" TRIPLICADO é = {float(numero) * 3}'


# def quadruplicar(numero):
#     return f'O número "{numero}" QUADRUPLICADO é = {float(numero) * 4}'


# print(duplicar(input('Digite um número: ')))
# print(triplicar(input('Digite um número: ')))
# print(quadruplicar(input('Digite um número: ')))

def multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(quadruplicar(5))
