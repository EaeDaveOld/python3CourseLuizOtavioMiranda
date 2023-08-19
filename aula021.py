# Logical operators - AND
# Operadores lógicos
# and (e) or (ou) not(não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualqeur valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy
# 0 0.0 '' False
# Também existe o tipo None que é
# Usado para representar um não valor

import time

print('### Sistema da Empresa X ###')
login = input('Digite a sua matrícula: ')
senha = input('Digite sua senha: ')

if login == '123' and senha == '321':
    print('Logando...')
    time.sleep(1)
    print('Logado no sistema com sucesso!')
else:
    print('Logando...')
    time.sleep(1)
    print('Usuário ou senha inválido.')


# Avaliação de curto circuito
print(True and True and True)  # Retorna True
print(True and 0 and True)  # Retorna 0
print(bool(0))  # Retorna False
print(bool(0.0))  # Retorna False
print(bool(''))  # Retorna False
