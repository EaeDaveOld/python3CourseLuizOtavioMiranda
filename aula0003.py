# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genério
# QLayout -> Um widget de layout que recebe outros widgets

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication()  # É o loop da aplicação, porém não exibe nada.

botao = QPushButton('Botão 1')  # Botão isolado
botao.setStyleSheet('font-size: 40px; color: red')
# botao.show()  # Adiciona o widget na hierarquia e exibe a janela

botao2 = QPushButton('Botão 2')  # Botão isolado
botao2.setStyleSheet('font-size: 20px; color: green')
# botao2.show()

botao3 = QPushButton('Botão 3')  # Botão isolado
botao3.setStyleSheet('font-size: 20px; color: black')

central_widget = QWidget()  # Widget genérico central que fará o controle geral
layout = QGridLayout()  # Definição do layout principal, que receberá outros widgets
central_widget.setLayout(layout)  # Setando o layout principal do QWidget()

layout.addWidget(botao, 1, 1)  # Add outros widgets no layout
layout.addWidget(botao2, 1, 2)
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show()  # Central widget entre na hierarquia e mostre a sua janela


app.exec()  # Executa o loop da aplicação
