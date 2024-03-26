from sys import path
# import aula099_package
import aula099_package.modulo  # 1
from aula099_package import modulo  # 2
from aula099_package import *  # Má prática de programação, importa tudo.
from aula099_package.modulo import soma_do_modulo  # 3


# print(*path, sep="\n")

print(aula099_package.modulo.soma_do_modulo(5, 5))  # 1
print(modulo.soma_do_modulo(5, 5))  # 2
print(soma_do_modulo(5, 5))  # 3
