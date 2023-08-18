# input Function

# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

#  A função input armazena sempre o valor como string, então deve-se converter para int ou float caso queira fazer operações matemáticas.
numero_1 = float(input('Digite um número: '))  # Typecasting str to float
numero_2 = float(input('Digite outro núemro: '))  # Typecasting str to float
print(f'A soma do número {numero_1} + o número {numero_2} é = a {numero_1 + numero_2}')  # Se os inputs não estivessem em coerção para float, seria concatenado as str.