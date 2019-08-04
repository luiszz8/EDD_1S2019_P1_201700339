class NodoS:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sig = None
        self.ant = None
class Serpiente:
    def __init__(self):
        self.inici = None
        self.fin = None

    def agregarFinal(self, node):
        if self.fin is None:
            self.fin = node
            self.inici = node
        else:
            self.fin.sig = node
            node.ant = self.fin
            self.fin = node

    def eliminarFinal(self):
        self.fin.ant.sig = None
        self.fin = self.fin.ant


    def print_list(self):
        if self.inici is None:  # verify if our CircularLinkedList is empty
            print('The list is empty')  # print a warning
        else:
            temp = self.inici
            while temp is not None:  # iterate our list printing each element-
                print(temp.x)  # -as we go
                temp = temp.sig


lista = Serpiente()
lista.agregarFinal(NodoS(1,2))
lista.agregarFinal(NodoS(4,2))
lista.agregarFinal(NodoS(5,2))
lista.eliminarFinal()
lista.agregarFinal(NodoS(7,2))
lista.agregarFinal(NodoS(8,2))
lista.print_list()