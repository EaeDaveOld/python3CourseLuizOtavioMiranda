# Iterating strings with while

"""
Iterando strings com while
"""
#       01234
nome = 'David'  # Iteráveis
#       54321
tamanho_nome = len(nome)  # 5 caracteres
print(nome)
print(tamanho_nome)

# Utilizando o while, crie essa nova string a partir da variavel nome
# nova_string = '*D*a*v*i*d'
nome = input('Digite o seu nome: ')
qtd_nome = len(nome)
nova_str = ''
index = 0

while index < qtd_nome:
    nova_str += '*' + nome[index]
    index += 1

print(nova_str)
