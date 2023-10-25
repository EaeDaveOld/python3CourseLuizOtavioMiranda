# 6 - Dada uma lista de números, crie uma nova lista contendo apenas os números pares e maiores que 10.

numeros = [numero for numero in range(101) if numero > 0]
print(numeros)

print()

pares_maior_dez = [numero for numero in numeros if numero %
                   2 == 0 and numero > 10]
print(pares_maior_dez)
