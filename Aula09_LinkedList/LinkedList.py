from no import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addNoInicio(self, valor):
        nodo = Node(valor)
        if self.head is not None:
            nodo.next = self.head
        self.head = nodo
        self.imprimir()

    def addNoFim(self, valor):
        nodo = Node(valor)
        if self.head == None:
            self.head = nodo
        elif self.head.next is None:
            self.head.next = None
        else:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = nodo
        self.imprimir()

    def removerDoInicio(self):
        if self.head != None:
            self.head = self.head.next
        self.imprimir()

    def removerDoFim(self):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                ant = self.head
                aux = self.head
                while aux.next:
                    ant = aux
                    aux = aux.next
                ant.next = None
            print("Elemento removido")
        self.imprimir()

    def imprimir(self):
        print("-----------------------------------------------")
        if self.head is None:
            print ("Lista encadeada vazia!")
        else:
            aux = self.head
            while aux:
                print(aux.value)
                aux = aux.next
    
  