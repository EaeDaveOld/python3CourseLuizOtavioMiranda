# advanced for loop

"""
Iterável -> strm range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o seu próximo valor
iter -> me entregue seu iterador
"""
texto = 'David'.__iter__()  # Método que retorna o iterator do objeto  -> .__iter__()
texto2 = iter('David')  # Mesma coisa que retorna o iterator do objeto, porém usando uma função
print(texto.__next__())  # D
print(texto.__next__())  # a
print(texto.__next__())  # v
print(texto.__next__())  # i
print(next(texto))  # d  -> same as texto.__next__()
print(texto2)

# for letra in nome
nome = 'David'  # iterável
iterador = iter(nome)  # iterator

# For how it works
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break


