# # from sys import path
# # import aula099_package
# import aula099_package.modulo  # 1
# from aula099_package import modulo  # 2
# from aula099_package import *  # Má prática de programação, importa tudo.
# from aula099_package.modulo import soma_do_modulo  # 3

# # ------------------------------------------
# # Foi importado o método fala_oi() do módulo modulo_2.py através de saltos.
# from aula099_package.modulo import fala_oi


# # print(*path, sep="\n")

# print(aula099_package.modulo.soma_do_modulo(5, 5))  # 1
# print(modulo.soma_do_modulo(5, 5))  # 2
# print(soma_do_modulo(5, 5))  # 3

# # Ao executar o método, o Python vai para o aula099_package.modulo
# # E lá dentro desse módulo, há uma importação do aula099_package.modulo_b
# fala_oi()

from aula099_package import fala_oi, soma_do_modulo
fala_oi()
print(soma_do_modulo(5, 5))
