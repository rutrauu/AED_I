from no import Node

class OrderedLinkedList:

   def __init__(self):
      self.head = None

   def imprimir(self):
        print("-----------------------------------------------")
        if self.head is None:
            print ("Lista encadeada vazia!")
        else:
            aux = self.head
            while aux:
                print(aux.value)
                aux = aux.next

   def add(self, valor):
      nodo = Node(valor)
      if self.head == None:
         self.head = nodo
      elif valor < self.head.value:
         nodo.next = self.head
         self.head = nodo
      else:
         ant = self.head
         aux = self.head.next
         while aux:
            if valor < aux.value:
               ant.next = nodo
               nodo.next = aux
               break
            else:
               ant = aux
               aux = aux.next
         if aux == None:
            ant.next = nodo

      self.imprimir()

   def remove(self, valor):
      removed = False
      if self.head:
         if valor == self.head.value:
            self.head = self.head.next
            removed = True
         else:
            ant = self.head
            aux = self.head.next
            while aux:
               if valor == aux.value:
                  ant.next = aux.next
                  removed = True
                  break
               else:
                  ant = aux
                  aux = aux.next
         if removed:
            print("Elemento ", valor, " removido")
         else:
            print("Elemento ", valor, " não encontrado")

      self.imprimir()
