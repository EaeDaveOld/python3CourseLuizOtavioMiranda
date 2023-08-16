# Isso é uma função print;
print(12, 34)
# Ela recebe os argumentos 12 e 34;
# Ao imprimir, o separado entre um argumento e o outro por padrão é um espaço vazio.

# Isso é outra função print;
print(56, 78, sep='')
# Ela recebe os argumentos 56 e 78;
# Foi definido o parâmetro sep para o valor vazio, então não haverá espaços entre os argumentos.

# Essa sequência de caracteres "\n" significa uma quebra de linha.
# Ou seja LF -> \n (Quebra de linha em sistemas Unix, Windows vem adotando esse padrão);
# CRLF -> \r\n (Os sistemas Windows antigo adotam esse modelo).

# Pode-se perceber que o parâmetro end define o que será feito no final da função;
print('O 123 a seguir vai ser impresso ao finalizar esse print pelo parâmetro "end", e não terá a quebra de linha', end='123')
