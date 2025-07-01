class FilaEspera:
    def __init__(self):
        self.fila = []

    def adicionar(self, apartamento):
        nova_fila = [None] * (len(self.fila) + 1)
        for i in range(len(self.fila)):
            nova_fila[i] = self.fila[i]
        nova_fila[len(self.fila)] = apartamento
        self.fila = nova_fila
        print(f"Apartamento {apartamento.numero_ap} adicionado à fila de espera.")

    def retirar(self, numero_vaga):
        if len(self.fila) == 0:
            print("Fila vazia.")
            return
        apartamento = self.fila[0]
        apartamento.numero_vaga = numero_vaga

        nova_fila = [None] * (len(self.fila) - 1)
        for i in range(1, len(self.fila)):
            nova_fila[i - 1] = self.fila[i]
        self.fila = nova_fila

        print(f"Apartamento {apartamento.numero_ap} recebeu a vaga {numero_vaga} e foi retirado da fila.")

    def imprimir(self):
        if len(self.fila) == 0:
            print("Fila de espera vazia.")
        else:
            print("Fila de espera:")
            for ap in self.fila:
                print(f"- Apartamento {ap.numero_ap}, Torre: {ap.torre.nome if ap.torre else 'Sem torre'}")