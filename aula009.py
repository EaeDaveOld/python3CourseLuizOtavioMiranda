# Arithimetic operators

adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 2.2  # float
print('Divisão', divisao)

divisao_inteira = 10 // 2.2
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 10  # resto da divisão
print('Módulo', modulo)

valor = 5
calculo = 10 % valor == 0
if calculo == True:
    print(f'O número 10 é divisível e múltiplo de {valor}.')
else:
    print(f'O número 10 não é divisível e múltiplo de {valor}')