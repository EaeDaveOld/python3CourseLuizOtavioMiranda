# Built-In and official documentation
"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'david Rodrigues'  # 15 caracteres
# string[3] = 'ABC'  # Não é possível atribuir um valor para uma string dessa forma.
print(string[3])

outra_variavel = f'{string[:3]}G2A{string[3:]}'
print(outra_variavel)

print(string.capitalize())  # Retorna o valor da string capitalizada
print(string.zfill(18))  # Preenche com zeros à esquerda de acordo com a quantidade de caracteres que possui a string