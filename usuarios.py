class NodoU:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sig = None
        self.ant = None

class usuarios:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def agregar(self, node):
        if self.inicio is None:
            self.inicio = self.fin = node
        else:
            self.fin.sig = node
            node.ant = self.fin
            node.sig = self.inicio
            self.fin = node

    

    def print_list(self):
        if self.inicio is None:  # verify if our CircularLinkedList is empty
            print('The list is empty')  # print a warning
        else:
            temp = self.inicio
            print(temp.nombre)
            temp = temp.sig
            while temp is not self.inicio:  # iterate our list printing each element-
                print(temp.nombre)  # -as we go
                temp = temp.sig

lista = usuarios()
lista.agregar(NodoU("Juan"))
lista.agregar(NodoU("Jua"))
lista.agregar(NodoU("Ju"))
lista.print_list()