# 1 - Crie uma lista com os números pares de 1 a 10.

numeros_pares = [numero for numero in range(
    11) if numero > 0 and numero % 2 == 0]
print(numeros_pares)
