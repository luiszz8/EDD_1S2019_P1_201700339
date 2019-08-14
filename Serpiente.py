import os


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
        self.repit = False
        self.direccion = ""
        self.usuAc = ""
        self.acumulado = 0
        self.velocidad = 100
        self.nivel = 1


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

    def reiniciar(self):
        while self.tam>3:
            self.eliminarFinal()

    def print_list(self):
        if self.inici is None:  # verify if our CircularLinkedList is empty
            print('The list is empty')  # print a warning
        else:
            temp = self.inici
            while temp is not None:  # iterate our list printing each element-
                print(temp.x)  # -as we go
                temp = temp.sig
    def graficar(self):
        pun1=0
        pun2=1
        actual = self.inici
        datos = "digraph G {\n"
        datos = datos + "node[shape = record, width = 2.3, height = 0.6];\n"
        datos = datos + "rankdir = LR;\n"
        while actual is not None:
            datos = datos + "nodo" +str(pun1) + "[label=\"" + str(actual.x) + "," + str(actual.y) + "\"];\n"
            if actual is self.fin:
                break
            if actual.sig is not None:
                datos = datos + "nodo" +str(pun1) + "->nodo"+str(pun2) + "\n"
                datos = datos + "nodo" + str(pun2) + "->nodo" + str(pun1) + "\n"
                pun1 = pun1 + 1
                pun2 = pun2 + 1
            actual = actual.sig
        datos = datos + "nodof [label=\" null  \"];\n"
        datos = datos + "nodo" + str(pun1) + "->nodof \n"
        datos = datos + "nodoi [label=\" null  \"];\n"
        datos = datos + "nodoi ->nodo0 \n"
        datos = datos + "}"
        f = open("otro.dot", "w")
        f.write(datos)
        f.close()
        os.system("dot -Tjpg otro.dot -o snake.jpg")
        os.system("snake.jpg")
