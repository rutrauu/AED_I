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


# Inicializar torres padrão
torre1 = Torre(1, "A", "Rua das Flores, 123")
torre2 = Torre(2, "B", "Avenida Central, 456")

lista_torres = [torre1, torre2]
apartamentos = []
fila_espera = FilaEspera()


def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Adicionar apartamento na fila de espera")
        print("2. Retirar apartamento da fila e atribuir vaga")
        print("3. Imprimir fila de espera")
        print("4. Listar apartamentos")
        print("5. Listar torres")
        print("6. Cadastrar nova torre")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ap = Apartamento.cadastrar(lista_torres)

            # Adicionar à lista geral de apartamentos sem append
            nova_lista = [None] * (len(apartamentos) + 1)
            for i in range(len(apartamentos)):
                nova_lista[i] = apartamentos[i]
            nova_lista[len(apartamentos)] = ap
            apartamentos[:] = nova_lista

            fila_espera.adicionar(ap)

        elif opcao == "2":
            num_vaga = input("Informe o número da vaga a ser atribuída: ")
            fila_espera.retirar(num_vaga)

        elif opcao == "3":
            fila_espera.imprimir()

        elif opcao == "4":
            if len(apartamentos) == 0:
                print("Nenhum apartamento cadastrado.")
            else:
                print("Apartamentos:")
                for ap in apartamentos:
                    print(ap)

        elif opcao == "5":
            if len(lista_torres) == 0:
                print("Nenhuma torre cadastrada.")
            else:
                print("Torres:")
                for torre in lista_torres:
                    print(torre)

        elif opcao == "6":
            nova_torre = Torre.cadastrar()
            nova_lista_torres = [None] * (len(lista_torres) + 1)
            for i in range(len(lista_torres)):
                nova_lista_torres[i] = lista_torres[i]
            nova_lista_torres[len(lista_torres)] = nova_torre
            lista_torres[:] = nova_lista_torres

            print("Torre cadastrada com sucesso!")

        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
