# list[] copy method
"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'David'
outro_nome = nome
nome = 'Luiz'
print(nome)
print(outro_nome)

lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()  # lista_b possui uma cópia do valor da lista_a
# lista_b = lista_a  # lista_b está apontado para o valor da lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_b)
