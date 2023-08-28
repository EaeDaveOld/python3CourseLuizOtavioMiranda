# for / in - Introduction

# Loop quando se tem X repetições, ou seja, não se sabe quantas repetições terão.
# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes +=1


# print('Aquele laço acima pode ter repetições infinitas')

texto = 'Python'
novo_texto = ''

for letra in texto:  # Para cada "letra" em "texto" então:
    novo_texto += f'*{letra}'
    print(letra)  # Print a letra, retorna para o loop, então print novamente a letra, até o fim.


print(novo_texto + '*')