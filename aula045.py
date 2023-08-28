# advanced for loop

"""
Iterável -> strm range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o seu próximo valor
iter -> me entregue seu iterador
"""
texto = 'David'.__iter__()  # Método que retorna o iterator do objeto  -> .__iter__()
texto2 = iter('David')  # Mesma coisa que retorna o iterator do objeto, porém usando uma função
print(texto)
print(texto2)

