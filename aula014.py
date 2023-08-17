# .format Method

a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}'
# Foi inserido os parâmetros nomeados:
formato = string.format(nome1=a, nome2=b, nome3=c)
# Parâmetro nome1 com o argumento a
# Parâmetro nome2 com o argumento b
# Parâmetro nome3 com o argumento c

print(formato)
