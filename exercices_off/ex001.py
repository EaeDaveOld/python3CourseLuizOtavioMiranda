'''
Escreva uma função em Python que recebe um número como parâmetro e retorna 
o dobro desse número. Em seguida, escreva um programa que pede ao usuário 
para digitar um número, chama a função para calcular o dobro do número digitado e exibe 
o resultado na tela.
'''


def dobro(numero):
    return numero * 2


print(f'{"#" * 5} Calcular o dobro de um número {"#" * 5}')
numero = float(input('Digite um número qualquer: '))
print(dobro(numero))
