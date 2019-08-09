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
            self.tam = self.tam +1
        else:
            node.sig = self.cima
            self.cima = node
            self.tam = self.tam + 1

    def eliminar(self):
        if self.cima is None:
            return
        elif self.cima.sig is None:
            self.cima = None
            self.tam = self.tam - 1
        else:
            self.cima = self.cima.sig
            self.tam = self.tam - 1

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

