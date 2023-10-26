# dir, hasattr e getattr em Python
string = 'David'

print(string)

if hasattr(string, 'upper'):
    print('Existe upper aqui.')
    print(string.upper())

print(getattr(string, 'upper')())
