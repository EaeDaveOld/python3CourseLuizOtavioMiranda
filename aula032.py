# Exercice - 3 Programs

# First Program
def ParImpar():
    """
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
    print('### Par ou Ímpar ###')
    try:
        numero = int(input('Digite um número inteiro: '))  # Recebe o número do usuário
        
        if numero % 2 ==0:
            print('O número é par')
        else:
            print('O número é ímpar')
    except ValueError:
        print('Não é um número inteiro')

# Second Program
def IdentificadorTempo():
    """
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11.59, Boa tarde 12-17.59 e Boa noite 18-23.59.
"""
    print('### Identificador de Tempo ###')
    try:
        hora = float(input('Digite que horas são agora, ex: 11.42: '))
        manha = hora >= 0 and hora <= 11.59
        tarde = hora >= 12 and hora <= 17.59
        noite = hora >= 18 and hora <= 23.59

        if manha:
            print('Bom dia :)')
        elif tarde:
            print('Boa tarde :)')
        elif noite:
            print('Boa noite :)')
        else:
            print('Não conheço essa hora.')
    except ValueError:
        print('Digite somente números.')

# Third Program
def TamanhoNomes():
    """
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
    print('### Tamanho de Nomes ###')
    nome = input('Digite seu primeiro nome: ')
    letras_quantidade = len(nome)
    
    if nome:
        if letras_quantidade <= 4:
            print(f'Seu nome é, {nome}, tem {letras_quantidade} letras, então é curto.')
        elif letras_quantidade >= 5 and letras_quantidade <= 6:
            print(f'Seu nome é {nome}, tem {letras_quantidade} letras, então é normal.')
        elif letras_quantidade > 6:
            print(f'Seu nome é {nome}, tem {letras_quantidade} letras, então é muito grande.')
    else:
        print('Digite alguma coisa.')

print('### Escolha entre os 3 programas listados abaixo ###')
print('[1] - Identificar Número (Par ou Ímpar)')
print('[2] - Identificar Tempo (Manhã, Tarde ou Noite)')
print('[3] - Identificar Tamanho de Nomes (Curto, Normal, Grande)')

opcao = input('Digite alguma das opções citadas, exemplo "1": ')
if opcao == '1':
    ParImpar()
elif opcao == '2':
    IdentificadorTempo()
elif opcao == '3':
    TamanhoNomes()
elif opcao != '1' or opcao != '2' or opcao != '3':
    print('Digite somente entre as opções, 1, 2 e 3.')