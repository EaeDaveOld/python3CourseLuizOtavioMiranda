import importlib  # Biblioteca responsável por reimportar um módulo

import aula098_m
print(aula098_m.variavel)

# Módulos em Python são Singleton (Só pode existir uma instância)
for i in range(10):

    # Usando esse método da lib, é solicitado explicitamente o recarregamento do módulo.
    importlib.reload(aula098_m)
    print(i)

print("Fim")
