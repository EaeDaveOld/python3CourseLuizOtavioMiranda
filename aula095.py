# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# try:
#     print(8/0)
# except ZeroDivisionError:
#     print("Não é possível dividir por zero.")

# print(123)
# raise ValueError("Deu erro")
# print(456)

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(f"'{n}' deve ser int ou float "
                        f"'{tipo_n.__name__}' enviado")
    return True


def nao_divide_por_zero(d):
    if d == 0:
        raise ZeroDivisionError("Você está tentando dividir por zero.")
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_divide_por_zero(d)
    return n / d


print(divide("asd", 5))
