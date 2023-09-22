# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

#     C = 5 * ((F-32) / 9).

print('Conversor de temperatura')
graus_f = float(input('Digite o valor da temperatura em Fahrenheint: '))
graus_c = 5 * ((graus_f-32) / 9)
print(f'{graus_f:.2f} Fahrenheit | Celcius {graus_c:.2f}')
