from car import Car

class FifoCarros:

    def __init__( self ):
        self.inicio = None
        self.fim = None

    def lavarCarro( self ):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            if self.inicio == None:
                self.fim = None
            print( "Lavando carro..." )
        else: 
            print( "Não carro para ser lavado." )
        self.imprimir()

    def adicionarAFila( self, modelo, ano, placa ):
        nodo = Car(  modelo, ano, placa )
        if self.inicio is None:
            self.inicio = nodo
        elif self.inicio.prox is None:
            self.inicio.prox = nodo
        else: 
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        self.fim = nodo
        self.imprimir()
    
    def imprimir( self ):
        print( "----- Fila para Lavagem de Carros -----" )
        if self.inicio is None:
            print( "Fila para lavagem está vazia!" )
        else:
            aux = self.inicio
            txt = ""
            while aux != None:
                txt += str( aux.modelo + ", " + aux.ano + ", " + aux.placa) + " - " 
                aux = aux.prox
            print( txt )