# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layour)
#               -> Widget1 (botao1)
#               -> Widget2 (botao2)
#               -> Widget3 (botao3)

#   -> show
# -> exec

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

app = QApplication()  # É o loop da aplicação, porém não exibe nada.
window = QMainWindow()
central_widget = QWidget()  # Widget genérico central que fará o controle geral
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela')

botao1 = QPushButton('Botão 1')  # Botão isolado
botao1.setStyleSheet('font-size: 40px; color: red')
# botao.show()  # Adiciona o widget na hierarquia e exibe a janela

botao2 = QPushButton('Botão 2')  # Botão isolado
botao2.setStyleSheet('font-size: 20px; color: green')
# botao2.show()

botao3 = QPushButton('Botão 3')  # Botão isolado
botao3.setStyleSheet('font-size: 20px; color: black')


layout = QGridLayout()  # Definição do layout principal, que receberá outros widgets
central_widget.setLayout(layout)  # Setando o layout principal do QWidget()

layout.addWidget(botao1, 1, 1)  # Add outros widgets no layout
layout.addWidget(botao2, 1, 2)
layout.addWidget(botao3, 3, 1, 1, 2)

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Selecione uma opção')


def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi trocado')
    print(123)


# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Qualquer coisa')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(lambda: slot_example(status_bar))


window.show()


app.exec()  # Executa o loop da aplicação
