# Try, except, else e finally

try:
    a = 18
    b = 0
    print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
    print(c)
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Uma variável não está definida.')
except (TypeError, IndexError):
    print('Ultrapassou o index máximo')
except Exception:
    print('ERRO DESCONHECIDO.')


print('CONTINUAR')
