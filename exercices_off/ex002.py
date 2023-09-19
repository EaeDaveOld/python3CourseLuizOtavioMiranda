'''
Escreva uma função em Python que recebe uma lista de números como parâmetro e 
retorna a média desses números. Em seguida, escreva um programa que pede ao usuário 
para digitar uma lista de números separados por vírgulas, 
chama a função para calcular a média desses números e exibe o resultado na tela.
A fórmula para calcular a média de uma lista de números é simples: basta somar todos os 
elementos da lista e dividir o resultado pelo número de elementos na lista. Matematicamente, 
a fórmula para calcular a média pode ser escrita da seguinte forma:

Média = (x1 + x2 + ... + xn) / n

Onde:

    x1, x2, ..., xn são os elementos da lista de números.
    n é o número de elementos na lista.
'''


# for numero in lista:
#     numeros_somados += float(numero)


def calcular_media(lista):
    try:
        numeros_somados = 0
        soma_completa = False
    # Enquanto a soma_completa for falsa
        while soma_completa is False:
            # Para cada número na lista
            for numero in lista:
                numeros_somados += float(numero)  # some cada um deles
            soma_completa = True  # Depois a soma_completa será verdadeira

            # Assim calculará o que foi especificado
            calculo = numeros_somados / len(lista)
            return calculo
    except:
        return 'Digite somente números separados por vírgulas.'


print('#' * 5, 'Calcular média', '#' * 5)
lista = input('Digite uma lista, separado por vírgula: ').split(',')
print(calcular_media(lista))
