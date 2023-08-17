# f-strings (string formatting) - Formatação de Strings

# Supondo que eu queira exibir no print a seguinte lógica:
# Meu nome é David, eu tenho 21 anos de idade.

nome = 'David'
idade = 21

# Pode-se fazer dessa forma:
print('Meu nome é ', nome, ', eu tenho ', idade, ' anos de idade.', sep='')

# Ou usando a f-string
print(f'Meu nome é {nome}, eu tenho {idade} anos de idade.')
