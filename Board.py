class NodoB:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
        self.sig = None

class Board:
    def __init__(self):
         self.inicio = None
         self.fin = None
         self.tam = 0

    def insertar(self, node):
        if self.inicio is None:
            self.inicio = node
        else:
            tem = self.inicio
            while tem.sig is not None:
                tem = tem.sig
            tem.sig = node
        self.tam = self.tam + 1

    def eliminar(self):
        if self.inicio is None:
            return
        elif self.inicio.sig is None:
            self.inicio = None
        else:
            self.inicio = self.inicio.sig

    def tamanyo(self):
        return self.tam

    def print_list(self):
        if self.inicio is None:  # verify if our CircularLinkedList is empty
            print('The list is empty')  # print a warning
        else:
            temp = self.inicio
            while temp is not None:  # iterate our list printing each element-
                print(temp.nombre)  # -as we go
                temp = temp.sig

lista = Board()
lista.insertar(NodoB("Luis", 2))
lista.insertar(NodoB("L", 2))
lista.insertar(NodoB("Lis", 2))
lista.eliminar()
lista.eliminar()
lista.insertar(NodoB("Lisa", 2))
lista.print_list()


