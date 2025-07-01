from Torre import Torre
from Apartamento import Apartamento
from FilaEspera import FilaEspera

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