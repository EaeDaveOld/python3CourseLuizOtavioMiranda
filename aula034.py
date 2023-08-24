# while - conditional repeat structure

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

# Quero imprimir a mesma coisa 50x

controle = 0  # Variável de controle

while controle < 50:  # Enquanto o controle for menor que x valor:
    controle = controle + 1  # Então controle passará a receber + 1 valor:
    print(controle)  # E imprimirá esse valor

condicao = True

# Infinity Looping
while condicao:
    nome = input('Digite seu nome: ')
    print(f'Muito prazer, {nome}!')
    
    if nome == 'sair':
        break

