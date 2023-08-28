# for + range(start, stop, step)
"""
For + Range
range -> range(start, stop, step)
"""

# Na função range(), o último dígito não é incluído, sou seja, range(10), vai até o 9
numeros = range(10)  # De 0 a 9
numeros2 = range(5, 10)  # De 5 a 9
numeros3 = range(5, 10, 2)  # De 5 a 9 pulando de 2 em 2
print(numeros)
print(numeros2)
print(numeros3)

print()
print()

for numero in numeros:
    print(numero)

print()
print()

for numero in numeros2:
    print(numero)

print()
print()

for numero in numeros3:
    print(numero)