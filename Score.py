class NodoSc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sig = None

class Score:
    def __init__(self):
        self.cima = None
        self.tam = 0

    def agregar(self, node):
        if self.cima is None:
            self.cima = node
        else:
            node.sig = self.cima
            self.cima = node

    def eliminar(self):
        if self.cima is None:
            return
        elif self.cima.sig is None:
            self.cima = None
        else:
            self.cima = self.cima.sig

    def tamnyo(self):
        return self.tam

    def print_list(self):
        if self.cima is None:  # verify if our CircularLinkedList is empty
            print('The list is empty')  # print a warning
        else:
            temp = self.cima
            while temp is not None:  # iterate our list printing each element-
                print(temp.x)  # -as we go
                temp = temp.sig

lista = Score()
lista.agregar(NodoSc(1,2))
lista.agregar(NodoSc(4,2))
lista.agregar(NodoSc(5,2))
lista.eliminar()
lista.eliminar()
lista.agregar(NodoSc(6,2))
lista.eliminar()
lista.eliminar()
lista.eliminar()
lista.eliminar()
lista.print_list()