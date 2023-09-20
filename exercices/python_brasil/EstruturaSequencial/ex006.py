# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

pi = math.pi

raio = float(input('Digite o raio de um círculo e será calculado sua área: '))
area = pi * raio ** 2
print(f'A área do raio {raio} é = {area:.2f}M quadrados')
