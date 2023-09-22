# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
print('Conversor de temperatura')
graus_c = float(input('Digite o valor da temperatura em °C: '))
graus_f = (graus_c * (9/5)) + 32
print(f'{graus_c:.2f}°C | {graus_f:.2f}°F')
