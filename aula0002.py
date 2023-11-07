# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication()  # É o loop da aplicação, porém não exibe nada.

botao = QPushButton('Botão 1')
botao.setStyleSheet('font-size: 40px; color: red')
botao.show()  # Adiciona o widget na hierarquia e exibe a janela

# botao2 = QPushButton('Botão 2')
# botao2.show()

app.exec()  # Executa o loop da aplicação
