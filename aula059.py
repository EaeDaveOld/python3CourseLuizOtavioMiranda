# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

p, b, *_, u = lista
print(p, u)

# Vai iterar cada nome na lista
for nome in lista:
    print(nome, end=' ')  # Parametro end vai finalizar com espaço

print()

# Vai iterar por cada nome na lista
print(*lista, sep='\n')
print(*string)
print(*tupla)
