# Exercice - Answer and question system
# Exercício - sistema de perguntas e respostas
import time as tempo
import os as sistema

acertos = 0

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print('#' * 5, '1° - Perguntas e Respostas', '#' * 5)
print(perguntas[0]['Pergunta'])
print(f'Opções: {perguntas[0]["Opções"]}')
pergunta_1 = input('Digite o valor: ')

opcoes_1 = perguntas[0]['Opções']

if pergunta_1 == '5':
    print('Resposta correta!')
    acertos += 1
elif pergunta_1 not in opcoes_1:
    print('Opção inválida!')
else:
    print('Resposta incorreta!')

tempo.sleep(2)
sistema.system('cls')

print('#' * 5, '2° - Perguntas e Respostas', '#' * 5)
print(perguntas[1]['Pergunta'])
print(f'Opções: {perguntas[1]["Opções"]}')
pergunta_2 = input('Digite o valor: ')

if pergunta_2 == '25':
    print('Resposta correta!')
    acertos += 1
elif pergunta_2 not in perguntas[1]['Opções']:
    print('Opção inválida!')
else:
    print('Resposta incorreta!')

tempo.sleep(2)
sistema.system('cls')


print('#' * 5, '3° - Perguntas e Respostas', '#' * 5)
print(perguntas[2]['Pergunta'])
print(f'Opções: {perguntas[2]["Opções"]}')
pergunta_2 = input('Digite o valor: ')

if pergunta_2 == '5':
    print('Resposta correta!')
    acertos += 1
elif pergunta_2 not in perguntas[2]['Opções']:
    print('Opção inválida!')
else:
    print('Resposta incorreta!')

tempo.sleep(2)
sistema.system('cls')

print(f'Você acertou {acertos} perguntas.')
