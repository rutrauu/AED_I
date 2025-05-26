import sys
from PyQt5.QtWidgets import *

from TelaVeiculo import TelaVeiculo
from TelaCarro import TelaCarro
from TelaCategoria import TelaCategoria

app = QApplication(sys.argv)

telaVeiculo = TelaVeiculo("Cadastro de Veículo")

telaVeiculo.show()

categorias = []
telaCat = TelaCategoria("Cadastro de categoria")

telaCarro = TelaCarro("Cadastro de Carro: ", categorias, telaCat )
telaCarro.show()

sys.exit( app.exec_() )