""" Calculadora com while"""

# Pedir 1° número para o usuário
# Pedir o 2° número para o usuário
# Pedir algum operador, ex: + - / *
# Fazer a operação entre o 1° número e o 2° número com o operador fornecido

while True:
    try:
        numero1 = float(input('Digite o 1° número: '))
        numero2 = float(input('Digite o 2° número: '))
        operador = input(f'O que você deseja fazer entre o número {numero1} e o {numero2} - Somar[+], Subtrair[-], Dividir[/] ou Multiplicar[*]: ').upper()
        
        if operador == '+' or operador == 'SOMAR':
            print(f'{numero1} + {numero2} = {numero1 + numero2}')
        elif operador == '-' or operador == 'SUBTRAIR':
            print(f'{numero1} - {numero2} = {numero1 - numero2}')
        elif operador == '/' or operador == 'DIVIDIR':
            print(f'{numero1} / {numero2} = {numero1 / numero2}')
        elif operador == '*' or operador == 'MULTIPLICAR':
            print(f'{numero1} * {numero2} = {numero1 * numero2}')
        else:
            print('Valor inválido, escolher entre Somar[+], Subtrair[-], Dividir[/] ou Multiplicar[*].')
            continue

        sair = input('Você quer sair? [S]im ou [N]ão: ').upper().startswith('S')  # Essa variável começa com 'S'? Se sim: True, se não: False
        if sair is True:
            break
        else:
            continue
    except ValueError:
        print('Erro - Digite somente números.')
