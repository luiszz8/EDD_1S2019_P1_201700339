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
        self.tam = 0
        self.agregarFinal(NodoS(7, 5))
        self.agregarFinal(NodoS(6, 5))
        self.agregarFinal(NodoS(5, 5))


    def agregarInicio(self, node):
        if self.fin is None:
            self.fin = node
            self.inici = node
            self.tam = self.tam+1
        else:
            self.fin.sig = node
            node.ant = self.fin
            node.sig = self.inici
            self.inici.ant = node
            self.inici = node
            self.tam = self.tam + 1

    def agregarFinal(self, node):
        if self.fin is None:
            self.fin = node
            self.inici = node
            self.tam = self.tam + 1
        else:
            self.fin.sig = node
            node.ant = self.fin
            self.fin = node
            self.tam = self.tam + 1

    def eliminarFinal(self):
        if self.tam >= 3:
            self.fin.ant.sig = None
            self.fin = self.fin.ant
            self.tam = self.tam - 1


    def print_list(self):
        if self.inici is None:  # verify if our CircularLinkedList is empty
            print('The list is empty')  # print a warning
        else:
            temp = self.inici
            while temp is not None:  # iterate our list printing each element-
                print(temp.x)  # -as we go
                temp = temp.sig


