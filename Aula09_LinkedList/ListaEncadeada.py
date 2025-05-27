from no import No

class ListaEncadeada:
    def __init__(self) -> None:
        self.inicio = None

    def addNoInicio(self, valor):
        nodo = No(valor)
        if self.inicio is not None:
            nodo.prox = self.inicio
        self.inicio = nodo
        self.imprimir()

    def addNoFim(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        elif self.inicio.prox is None:
            self.inicio.prox = None
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        self.imprimir()

    def removerDoInicio(self):
        if self.inicio != None:
            self.inicio = self.inicio.prox
        self.imprimir()

    def removerDoFim(self):
        if self.inicio != None:
            if self.inicio.prox == None:
                self.inicio = None
            else:
                ant = self.inicio
                aux = self.inicio
                while aux.prox:
                    ant = aux
                    aux = aux.prox
                ant.prox = None
            print("Elemento removido")
        self.imprimir()

    def imprimir(self):
        print("-----------------------------------------------")
        if self.inicio is None:
            print ("Lista encadeada vazia!")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado)
                aux = aux.prox
    
  