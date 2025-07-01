class Apartamento:
    def __init__(self, id, numero_ap, numero_vaga=None, torre=None):
        self.id = id
        self.numero_ap = numero_ap
        self.numero_vaga = numero_vaga
        self.torre = torre

    def __str__(self):
        vaga_str = f"Vaga: {self.numero_vaga}" if self.numero_vaga is not None else "Sem vaga"
        torre_str = self.torre.nome if self.torre else "Sem torre"
        return f"Apartamento {self.numero_ap} (ID: {self.id}), {vaga_str}, Torre: {torre_str}"

    @classmethod
    def cadastrar(cls, lista_torres):
        id_ap = int(input("ID do apartamento: "))
        num_ap = input("Número do apartamento: ")

        print("Escolha a torre:")
        for i in range(len(lista_torres)):
            print(f"{i+1} - {lista_torres[i].nome}")

        escolha = int(input("Número da torre: "))
        torre_escolhida = lista_torres[escolha - 1]

        return cls(id_ap, num_ap, None, torre_escolhida)