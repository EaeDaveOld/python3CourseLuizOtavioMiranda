s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
# print(s1)
# print(s1)
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  # UNIÃO
s3 = s1 & s2  # INTERSECÇÃO
s3 = s1 - s2  # DIFERENÇA
s3 = s1 ^ s2  # DIFERENÇA SIMÉTRICA
print(s3)
