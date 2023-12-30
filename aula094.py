# try, except, else e finally
# valor = 10
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:   # Só será executado a linha abaixo, os códigos que não ocorrerem nenhum erro.
    print("A variável valor é igual a 10, e não será executada pois não foi declarada, está como um comentário.")
    print(valor)
# Caso ocorra uma exceção, qualquer erro... O código abaixo será executado.
except NameError as NomeError:
    print(NomeError.__class__.__name__)
    print(NomeError)
else:  # O else fará o contrário do argumento anterior, ou seja, só executará se não houver nenhum except.
    print("Não deu erro.")
finally:  # Essa linha de código sempre será executada.
    print("Aqui sempre será executado, está em finally.")
