# Exercice IF & Relational Operators

# Crie um algoritmo que leia dois números fornecidos pelo usuário
# Verifique se o primeiro é maior do que o segundo ou igual
# Mostre na tela formatado.

print('### Comparador de números ###')
numero1 = input('Digite o 1° número: ')
numero2 = input('Digite o 2° número: ')

if numero1 > numero2:
    print(f'O número {numero1} é maior do que o número {numero2}')
elif numero1 < numero2:
    print(f'O número {numero1} é menor do que o número {numero2}')
elif numero1 == numero2:
    print(f'O número {numero1} é igual ao número {numero2}')