class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return f"Torre {self.nome} (ID: {self.id}), Endereço: {self.endereco}"

    @classmethod
    def cadastrar(cls):
        id_torre = int(input("ID da torre: "))
        nome = input("Nome da torre: ")
        endereco = input("Endereço da torre: ")
        return cls(id_torre, nome, endereco)

   