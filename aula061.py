# Exercice - First CPF Digit Validator

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

CPF = '746824890'
print('Validando o primeiro dígito do CPF')

soma_total = 0

for indice, numero in zip(range(10, -1, -1), CPF):
    inteiro_indice = int(indice)
    inteiro_numero = int(numero)
    calculo = inteiro_indice * inteiro_numero

    soma_total += calculo

    print(f'{indice} * {numero} = {calculo}')

multi_por_10 = soma_total * 10
resto_por_11 = multi_por_10 % 11

print(f'A soma total é = {soma_total}')
print(f'A soma total é = {multi_por_10}')
print(f'A soma total é = {resto_por_11}')

if resto_por_11 > 9:
    digito = 0
else:
    digito = resto_por_11

print(f'O primeiro dígito do CPF é = {digito}')
