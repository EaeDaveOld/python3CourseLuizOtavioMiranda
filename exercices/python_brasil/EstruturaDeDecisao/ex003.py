# Exercice - Checking sex

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite [M] para masculino e [F] para feminino: ').upper()
if sexo == 'M':
    print('Você é do sexo Masculino.')
elif sexo == 'F':
    print('Você é do sexo Feminino.')
else:
    print('Opção inválida, digite somente "M" ou "F"')
