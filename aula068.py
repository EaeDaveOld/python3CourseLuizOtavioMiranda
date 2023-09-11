# Scope of functions - Global & Local

"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1  # Global


def escopo():
    x = 10  # Essa variável foi declarada no escopo da função.

    def outra_funcao():
        y = 2
        print(x, y)
    outra_funcao()


escopo()
print(x)
