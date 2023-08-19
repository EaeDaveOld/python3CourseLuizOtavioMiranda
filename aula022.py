# Logical operators - OR
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
login = input('Digite seu login: ')
senha = input('Digite sua senha: ')

# Colocando a condição or
# Então será avaliado
# Se as outras opções são verdadeiras
# login == David ou DAVID ou david -> VERDADEIRO e senha == '321' -> VERDADEIRO
if (login == 'David' or login == 'DAVID' or login == 'david') and senha == '321':
    print('Logando...')
    time.sleep(1)
    print('Logado no sistema com sucesso!')
else:
    print('Logando...')
    time.sleep(1)
    print('Usuário ou senha inválido.')


# Avaliação de curto circuito
print(True or True)  # True
print(True or False)  # True
print(False or False)  # False
print(False or True)  # True
