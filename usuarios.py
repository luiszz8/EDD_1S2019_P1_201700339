import os


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
            self.inicio.ant = self.fin



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

    def graficar(self):
        pun1=0
        pun2=1
        actual = self.inicio
        datos = "digraph G {\n"
        datos = datos + "node[shape = record, width = 2.3, height = 0.6];\n"
        #datos = datos + "rankdir = LR;\n"
        while actual is not self.fin:
            datos = datos + "nodo" +str(pun1) + "[label=\"" + actual.nombre + "\"];\n"
            datos = datos + "nodo" +str(pun1) + "->nodo"+str(pun2) + "\n"
            datos = datos + "nodo" + str(pun2) + "->nodo" + str(pun1) + "\n"
            pun1 = pun1 + 1
            pun2 = pun2 + 1
            actual = actual.sig
        datos = datos + "nodo" + str(pun1) + "[label=\"" + actual.nombre + "\"];\n"
        datos = datos + "nodo0 -> nodo" + str(pun1) + "\n"
        datos = datos + "nodo" + str(pun1) + "-> nodo0 \n"
        datos = datos + "}"
        f = open("otro4.dot", "w")
        f.write(datos)
        f.close()
        os.system("dot -Tjpg otro4.dot -o usuar.jpg")
        os.system("usuar.jpg")


