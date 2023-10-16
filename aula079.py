# sets examples
# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite uma letra: ').lower()
    letras.add(letra)
    print(letras)

    if 'l' in letras:
        print('PARABÉNS, VOCÊ ENCONTROU A LETRA MISTERIOSA!')
        break
