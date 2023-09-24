# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite seu peso: '))
print('[H]omem')
print('[M]ulher')
sexo = input('Digite seu sexo: ').lower()

peso_ideal_homem = 72.7 * altura - 58
peso_ideal_mulher = 62.1 * altura - 44.7

if sexo.startswith('h'):
    print(
        f'Você é homem, tem {altura}M de altura e seu peso ideal é {peso_ideal_homem:.2f}Kg.')
elif sexo.startswith('m'):
    print(
        f'Você é mulher, tem {altura}M de altura e seu peso ideal é {peso_ideal_mulher:.2f}Kg.')
else:
    print('Valor inválido, digite somente entre [H]omem] e [M]ulher.')
