import sys
from PyQt5.QtWidgets import *

from TelaVeiculo import TelaVeiculo
from Carro import Carro

class TelaCarro(TelaVeiculo):
    def __init__(self, titulo = "Tela de Carro", categorias = [], telaCat = None):
        self.listaCategorias = categorias
        self.telaCategoria = telaCat
        super().__init__(titulo)
        self.setGeometry(1300, 600, 300, 300)

    def definirLayout(self):
        super().definirLayout()
        self.lblPortas = QLabel("Portas: ")
        self.txtPortas = QLineEdit(self)
        self.layout.addWidget(self.lblPortas)
        self.layout.addWidget(self.txtPortas)

        self.lblCategoria = QLabel("Categoria")
        self.layout.addWidget(self.lblCategoria)

        self.cmbCategoria = QComboBox(self)
        self.carregarCategorias()
        self.layout.addWidget(self.cmbCategoria)

        self.btnAbrirTelaCat = QPushButton("Add Categoria", self)
        self.btnAbrirTelaCat.clicked.connect(self.abrirTelaCategoria)
        self.layout.addWidget(self.btnAbrirTelaCat)

    def abrirTelaCategoria(self):
        self.telaCategoria.show()

    def carregarCategorias(self):
        self.cmbCategoria.addItem("Selecione...", None)
        for cat in self.listaCategorias:
            self.cmbCategoria.addItem(cat.nome, cat)
        
    def salvar(self):
        modelo = self.txtModelo.text()
        ano = self.txtAno.text()
        if (ano != ""):
            ano = int(ano)
        portas = self.txtPortas.text()
        if portas != "":
            portas = int (portas)
        carro = Carro(modelo, ano, portas)
        QMessageBox.information(self, "Carro salvo!" + str(carro))

        