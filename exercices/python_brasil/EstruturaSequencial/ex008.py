# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print('Calculadora de salário')
ganho_por_hora = float(
    input('Digite o valor que você ganhar por hora em R$: '))
horas_trabalhadas = float(
    input('Digite a quantidade de horas trabalhadas no mês: '))
salario_mes = ganho_por_hora * horas_trabalhadas

print(f'Você recebe {salario_mes}R$ por mês.')
