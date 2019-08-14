import os


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
        if self.tam == 10:
            self.eliminar()
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
        self.tam = self.tam - 1

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


    def graficar(self):
        pun1=0
        pun2=1
        actual = self.inicio
        datos = "digraph G {\n"
        datos = datos + "node[shape = record, width = 2.3, height = 0.6];\n"
        datos = datos + "rankdir = LR;\n"
        while actual is not None:
            datos = datos + "nodo" +str(pun1) + "[label=\"" + actual.nombre + "," + str(actual.puntaje) + "\"];\n"
            if actual.sig is not None:
                datos = datos + "nodo" +str(pun1) + "->nodo"+str(pun2) + "\n"
                pun1 = pun1 + 1
                pun2 = pun2 + 1
            actual = actual.sig
        datos = datos + "nodof [label=\" null  \"];\n"
        datos = datos + "nodo" + str(pun1) + " -> nodof \n"
        datos = datos + "}"
        f = open("otro2.dot", "w")
        f.write(datos)
        f.close()
        os.system("dot -Tjpg otro2.dot -o board.jpg")
        os.system("board.jpg")


