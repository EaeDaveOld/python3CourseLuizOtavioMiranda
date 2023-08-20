"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a  __repr__ __str__ 
"""

variavel = 'OI'
# print(f'{variavel}')
print(f'{variavel: >10} foram colocados 10 caracteres de "ESPAÇO" à ESQUERDA antes da variavel')
print(f'{variavel: <10} foram colocados 10 caracteres de "ESPAÇO" à DIREITA DEPOIS da variavel')
print(f'{variavel:x^10} a variavel passou a ter 10 caracteres totais e o valor dela ficou no CENTRO e as demais foram substituídas por "x"')
print(f'{1000.81290348:,.1f}')

print(f'{variavel!r}')
