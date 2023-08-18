# Conditional - if, elif, else

# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair?" ')

if entrada == 'entrar':  # Se o valor da variável entrada for 'entrar', logo será True, e interpretará o código abaixo:
    print('Você entrou no sistema.')
elif entrada == 'sair':  # Se o valor for 'sair', então interpretará o código abaixo:
    print('Você saiu do sistema.')
else:  # Se o valor da variável entrada não for nem 'entrar' e nem 'sair', então será falso, exibindo o código abaixo:
    print('Você digitou uma opção inválida.')


print('FORA DOS BLOCOS')