# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado positivo.

print(f'11 é um número do tipo {type(11)}')  # int
print(f'assim como -11 é do tipo {type(-11)}')  # int
print(0)  # int

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
# A função type mostra o tipo que o Python
# inferiu ao valor.

print(f'1.1 e 10.11 é do tipo {type(1.1), type(10.11)}')  # float
print(-1.0)  # float

float_negative = -1.0
print(type(float_negative))
