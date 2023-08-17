# Variables

# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

nome_completo = 'David Rodrigues da Silva'  # O nome da varíavel é "nome_completo"
print(nome_completo)  # Ao chamar a variável "nome_completo" dentro da função print, obtem-se o valor dela.

soma_dois_mais_dois = 2 + 2
print(soma_dois_mais_dois)  # = 4

numero = int(input('Digite um número qualquer: '))  # A variável numero vai armazenar o valor digitado pelo usuário
quadrado = numero ** 2  # A variável quadrado está armazenada a expressão numero elevado (**) a 2
print(f'O número {numero} elevado ao quadrado é = {quadrado}')  # Está sendo chamado as variáveis numero e quadrado nessa expressão

nome = 'David'
idade = 21
maior_de_idade = idade >= 18

print(f'Olá, {nome}, você tem {idade} anos de idade, maior de idade?: {maior_de_idade}')  # Mesmo resultado do que o abaixo
print('Olá, {}, você tem {} anos de idade, maior de idade?: {}'.format(nome, idade, maior_de_idade))  # Mesmo resultado do que o acima
