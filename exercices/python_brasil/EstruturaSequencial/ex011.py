# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

#     o produto do dobro do primeiro com metade do segundo .
#     a soma do triplo do primeiro com o terceiro.
#     o terceiro elevado ao cubo.

inteiro_1 = int(input('Digite um número inteiro: '))
inteiro_2 = int(input('Digite outro número inteiro: '))
real_1 = float(input('Digite um número real: '))

print((inteiro_1 * 2) * (inteiro_2 / 2))
print((inteiro_1 * 3) + real_1)
print(f'{real_1 ** 3}')
