# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('Digite a nota do 1° bimestre: '))
nota2 = float(input('Digite a nota do 2° bimestre: '))
nota3 = float(input('Digite a nota do 3° bimestre: '))
nota4 = float(input('Digite a nota do 4° bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A nota média foi igual a = {media}')