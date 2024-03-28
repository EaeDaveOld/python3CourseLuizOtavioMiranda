# from .modulo import soma_do_modulo, fala_oi
# Esse arquivo é inicializado, assim que o pacote aula099_package for importado.
from aula099_package.modulo import *  # Então será importado tudo do modulo.py
from aula099_package.modulo_b import *  # E tudo do modulo_b.py

print("Você importou", __name__)


def dobra(x):
    return x * 2
