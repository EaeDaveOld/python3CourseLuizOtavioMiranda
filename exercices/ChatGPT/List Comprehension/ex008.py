# 8 - Dada uma lista de frutas, crie uma nova lista com o comprimento de cada fruta, apenas para as frutas com mais de 5 letras.

frutas = ['Maça', 'Banana', 'Pera', 'Abacaxi', 'Manga', 'Jabuticaba']

comprimento_maior_cinco = [
    fruta.__len__() for fruta in frutas if fruta.__len__() > 5]
print(comprimento_maior_cinco)
