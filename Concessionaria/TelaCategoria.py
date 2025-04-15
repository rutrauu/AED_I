import sys
from PyQt5.QtWidgets import *

from Categoria import Categoria
from TelaCarro import TelaCarro

class TelaCategoria(QMainWindow):
    def __init__(self, titulo = "Tela Categoria", categorias = [], TelaCarro = None):
        self.listaCategorias = categorias
        self.TelaCarro = TelaCarro
        super().__init__()

        self.setWindowTitle(titulo)
        self.setGeometry(120,180,490,405)
        self.layout = QVBoxLayout()

        self.definirLayout()

        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.clicked.connect(self.__salvar)
        self.layout.addWidget(self.btnSalvar)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        
    def definirLayout(self):
        self.lblNome = QLabel("Nome: ")
        self.txtNome = QLineEdit(self)
        self.layout.addWidget(self.lblNome)
        self.layout.addWidget(self.txtNome)

    def __salvar(self):
        nome = self.txtNome.text()
        if (nome != " "):
            cat = Categoria(nome)
            self.listaCategorias.append(cat)
            self.TelaCarro.carregarCategorias()
        QMessageBox.information(self, "Categoria salva!" + str(cat))

        