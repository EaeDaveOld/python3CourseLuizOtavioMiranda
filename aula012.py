# Exercice - BMI Calculation (Cálculo do IMC) + Ellipsis

nome = 'David Rodrigues'
altura = 1.70
peso = 65
imc = ...  # Ellipsis (...) Não chega a dar erro no code, serve para dar valor a algo temporariamente)

# David Rodrigues tem 1.70 de altura,
# pesa 65 quilos e seu IMC é
# 22.49

nome = 'David Rodrigues'
altura = 1.70
peso = 65
imc = peso / (altura * altura)  # O IMC calcula-se dividindo o peso pelo quadrado da altura
print(f'{nome} tem {altura}M de altura, {peso}KG de peso e seu IMC é de: {imc}')
