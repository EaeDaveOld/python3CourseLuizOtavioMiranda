# Salary Calculator

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

ganho_hora = float(input('Quanto você ganha por hora: '))
mes_horas_trabalhadas = float(input('Quantas horas você trabalhou no mês: '))
salario_bruto = ganho_hora * mes_horas_trabalhadas
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
SINDICATO = salario_bruto * 0.05
salario_liquido = salario_bruto - IR - INSS - SINDICATO
print(f'+ Salário Bruto: R${salario_bruto}')
print(f'- IR: R${IR}')
print(f'- INSS: R${INSS}')
print(f'- Sindicato: R${SINDICATO}')
print(f'= Salário Liquido: R${salario_liquido}')
