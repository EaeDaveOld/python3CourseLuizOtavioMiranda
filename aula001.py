# Comments in Python
# Isso é um comentário em Python e não será interpretado pelo interpretador do mesmo.

print('Acima, há um comentário que não foi interpretado, portanto, teoricamente não existe nessa instância. ')


def docstring():  # Aqui há uma função definida pelo usuário chamada docstring, e contém somente um docstring explicando o que o próprio recurso é.
    """
    - Isso é uma Docstring;
    - Não é comentário como o #;
    - O interpretador do Python interpreta, porém não exibe nada inicialmente a não ser que seja requisitado;
    - Consome recurso computacional, mesmo sendo mínimo;
    - É usada para documentar funções, classes, módulos ou método;
    """


print('Abaixo há uma Docstring que pode ser solicitada para mostrar uma explicação.')
print(docstring.__doc__)
