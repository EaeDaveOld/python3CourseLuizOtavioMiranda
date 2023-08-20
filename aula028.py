"""
Exercício
Peça ao usuário para digitar seu nome [CHECK]
Peça ao usuário para digitar sua idade [CHECK]
Se nome e idade forem digitados: [CHECK]
    Exiba:
        Seu nome é {nome} [CHECK]
        Seu nome invertido é {nome invertido} [CHECK]
        Seu nome contém (ou não) espaços [CHECK]
        Seu nome tem {n} letras [CHECK]
        A primeira letra do seu nome é {letra} [CHECK]
        A última letra do seu nome é {letra} [CHECK]
Se nada for digitado em nome ou idade:  [CHECK]
    exiba "Desculpe, você deixou campos vazios." [CHECK]
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

# 01234
# David
# -54321

if nome and idade:
    print(f'Seu nome é "{nome}"')
    print(f'Seu nome invertido é "{nome[::-1]}"')

    # Se estiver ' ' (espaço) em variavel "nome" então:
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')

    print(f'Seu nome tem "{len(nome)}" letras')
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A útlima letra do seu nome é "{nome[-1]}"')
else:
    print('Desculpe, você digitou campos vazios, tente novamente.')
