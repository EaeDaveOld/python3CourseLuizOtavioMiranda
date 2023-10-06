# Exercice - Vowel or Consoant
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
letra = input('Digire uma letra qualquer: ').lower()

if letra in vogais:
    print(f'A letra "{letra}" é vogal.')
elif letra in consoantes:
    print(f'A letra "{letra}" é consoante.')
else:
    print("Valor incorreto.")
