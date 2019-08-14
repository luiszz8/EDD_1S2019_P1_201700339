import curses
import curses.textpad
from Score import Score, NodoSc
from Serpiente import Serpiente, NodoS
from usuarios import usuarios, NodoU
from random import randint, uniform, random
from Board import Board, NodoB

menu = ['Play', 'Scoreboard', 'User Selection', 'Reports', 'Bulk Loading']
meReport = ['SNAKE REPORT', 'SCORE REPORT', 'SCOREBOARD REPORT', 'USERS REPORT', 'REGRESAR']
usu = usuarios()
usu.agregar(NodoU("Juan"))
usu.agregar(NodoU("Luis"))
usu.agregar(NodoU("Jorge"))
serp = Serpiente()
puntaj = 0
score = Score()
usuarioAct = "us"
tablero = Board()
golbale = False


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def print_mre(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(meReport):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def pintarUsu(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def print_board(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    temb = tablero.inicio
    y = 10
    t = w // 2 - len("Puntajes") // 2
    stdscr.addstr(5, t, "Puntajes")
    while temb is not None:
        x = w // 2 - len(temb.nombre) // 2
        stdscr.addstr(y, 30, temb.nombre)
        stdscr.addstr(y, 30 + 20, str(temb.puntaje))
        y = y + 1
        temb = temb.sig
    stdscr.refresh()

def cargar(ruta):
    f = open(ruta, "r")
    lineas = f.read().splitlines()
    lineas.pop(0)
    for l in lineas:
        linea = l.split(',')
        usu.agregar(NodoU(linea[0]))

def juego(stdscr,text,puntos,seguir):
    stdscr = curses.initscr()
    height = 20
    width = 60
    pos_y = 0
    pos_x = 0
    pause = False
    window = curses.newwin(height, width, pos_y, pos_x)  # create a new curses window
    td = curses.textpad.Textbox(window)
    nuevo =""
    if text == " " and serp.repit is False:
        td.edit()
        nuevo = td.gather()
        usu.agregar(NodoU(nuevo))
    else:
        nuevo = text
    window.keypad(True)  # enable Keypad mode
    curses.noecho()  # prevent input from displaying in the screen
    curses.curs_set(0)  # cursor invisible (0)
    window.border(0)  # default border for our window
    window.nodelay(True)  # return -1 when no key is pressed
    window.addstr(0, 3, 'Score:' + str(puntos))
    window.addstr(0, 20, 'SnakePro')
    window.addstr(0, 40, 'usuario:' + nuevo )
    key = curses.KEY_RIGHT  # key defaulted to KEY_RIGHT
    if serp.repit is False:
        pos_x = 7  # initial x position
        pos_y = 5  # initial y position
    else:
        pos_x = serp.inici.x  # initial x position
        pos_y = serp.inici.y
        if serp.direccion == "izquierda":
            key = curses.KEY_LEFT
        elif serp.direccion == "arriba":
            key = curses.KEY_UP
        elif serp.direccion == "abajo":
            key = curses.KEY_DOWN
    NpintI = serp.inici
    crece = False
    if seguir is False:
        while NpintI is not None:  # iterate our list printing each element-
            window.addch(NpintI.y, NpintI.x, '#')
            NpintI = NpintI.sig
    itemy = randint(2, 18)
    itemx = randint(2, 58)
    signo = randint(0, 1)
    while itemx == 5 or itemx == 6 or itemx == 7:
        itemx = randint(2, 58)
    if signo == 0:
        window.addch(itemy, itemx, '+')
        crece = True
    else:
        window.addch(itemy, itemx, '*')
        crece = False
    tiempo = serp.velocidad
    serp.repit = False
    while key != 27:  # run program while [ESC] key is not pressed
        if score.tam == 15:
            if serp.nivel == 1:
                serp.velocidad = 20
                tiempo = serp.velocidad
                tempC = serp.inici
                while tempC is not None:  # iterate our list printing each element-
                    window.addch(tempC.y, tempC.x, ' ')
                    tempC = tempC.sig
                serp.reiniciar()
            serp.nivel = 2
        window.timeout(tiempo)  # delay of 100 milliseconds
        keystroke = window.getch()  # get current key being pressed
        if keystroke is not -1:  # key is pressed
            key = keystroke  # key direction changes
        if key == 112:
            serp.repit = True
            serp.usuAc = nuevo
            serp.acumulado = puntos
            break

        if key == curses.KEY_RIGHT:  # right direction
            pos_x = pos_x + 1  # pos_x increase
            serp.direccion = "derecha"
        elif key == curses.KEY_LEFT:  # left direction
            pos_x = pos_x - 1  # pos_x decrease
            serp.direccion = "izquierda"
        elif key == curses.KEY_UP:  # up direction
            pos_y = pos_y - 1  # pos_y decrease
            serp.direccion = "arriba"
        elif key == curses.KEY_DOWN:  # down direction
            pos_y = pos_y + 1  # pos_y increase
            serp.direccion = "abajo"

        window.addch(serp.fin.y, serp.fin.x, ' ')

        if pos_x > 58:
            pos_x = 1
        if pos_x < 1:
            pos_x = 58
        if pos_y > 18:
            pos_y = 1
        if pos_y < 1:
            pos_y = 18
        serp.agregarInicio(NodoS(pos_x, pos_y))
        serp.eliminarFinal()



        if itemx == pos_x and itemy == pos_y and crece == True:
            score.agregar(NodoSc(itemx, itemy))
            puntos = puntos + 1
            nuevax = serp.fin.x - 1
            if nuevax == serp.fin.ant.x:
                nuevax = nuevax + 2
            serp.agregarFinal(NodoS(nuevax, serp.fin.y))
            itemy = randint(2, 18)
            itemx = randint(2, 58)
            signo = randint(0, 1)
            repex = False
            temS = serp.inici
            while not repex:
                repex = True
                while temS.sig is not None:
                    if temS.x == itemx:
                        repex = False
                    temS = temS.sig
                itemx = randint(2, 58)
            if signo == 0:
                window.addch(itemy, itemx, '+')
                crece = True
            else:
                window.addch(itemy, itemx, '*')
                crece = False

        if itemx == serp.inici.x and itemy == serp.inici.y and not crece:
            score.eliminar()
            if serp.tam > 3:
                puntos = puntos - 1
                window.addch(serp.fin.y, serp.fin.x, ' ')
                serp.eliminarFinal()
            itemy = randint(2, 18)
            itemx = randint(2, 58)
            signo = randint(0, 1)
            repex = False
            temS = serp.inici
            while not repex:
                repex = True
                while temS.sig is not None:
                    if temS.x == itemx:
                        repex = False
                        temS = temS.sig
                    itemx = randint(2, 58)
                if signo == 0:
                    window.addch(itemy, itemx, '+')
                    crece = True
                else:
                    window.addch(itemy, itemx, '*')
                    crece = False

        tempI = serp.inici
        while tempI is not None:  # iterate our list printing each element-
                window.addch(tempI.y, tempI.x, '#')
                tempI = tempI.sig
        window.addstr(0, 3, 'Score:' + str(puntos))
        fin = True
        temF = serp.inici.sig
        while temF.sig is not None:
            if temF.x == serp.inici.x and temF.y == serp.inici.y:
               fin = False
            temF = temF.sig
        if not fin:
            stdscr.clear()
            tablero.insertar(NodoB(nuevo, puntos))
            print_center(stdscr, "Tuvo " + str(puntos) + " puntos")
            key = stdscr.getch()
            serp.reiniciar()
            serp.acumulado = 0
            serp.usuAc = ""
            break
        if pause is True:
            break
    main(stdscr)

def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu

    print_menu(stdscr, current_row)
    elegir = False
    usa = ' '
    if serp.usuAc is not "":
        usa = serp.usuAc
    while 1:
        if not elegir:
            key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif current_row == 2 and elegir == True:
            tem = usu.inicio
            while key != curses.KEY_DOWN:

                if key == curses.KEY_RIGHT:
                    tem = tem.sig
                    print_center(stdscr, tem.nombre)
                elif key == curses.KEY_LEFT:
                    tem = tem.ant
                    print_center(stdscr, tem.nombre)

                key = stdscr.getch()
                usa = tem.nombre
            elegir = False
            key = stdscr.getch()
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 2:
                print_center(stdscr, usu.inicio.nombre)
                elegir = True
            elif current_row == 0:
                if serp.repit is True:
                    juego(stdscr, usa, serp.acumulado, golbale)
                else:
                    juego(stdscr, usa, puntaj, golbale)
            elif current_row == 1:
                print_board(stdscr)
            elif current_row == 4:
                stdscr.clear()
                tf = curses.textpad.Textbox(stdscr)
                archi = ""
                tf.edit()
                archi = tf.gather()
                j = archi.split(" ")
                cargar(j[0]+".csv")
            elif current_row == 3:
                salirR = True
                print_mre(stdscr, 0)
                fila = 0
                while salirR:
                    keyR = stdscr.getch()
                    if keyR == curses.KEY_UP and fila > 0:
                        fila -= 1
                    elif keyR == curses.KEY_DOWN and fila < len(meReport) - 1:
                        fila += 1
                    elif keyR == curses.KEY_ENTER or keyR in [10, 13]:
                        if fila == 0:
                            serp.graficar()
                        if fila == 1:
                            score.graficar()
                        if fila == 2:
                            tablero.graficar()
                        if fila == 3:
                            usu.graficar()
                        if fila == 4:
                            salirR = False
                    print_mre(stdscr, fila)

            else:
                print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            stdscr.getch()
            # if user selected last row, exit the program
            #if current_row == len(menu) - 1:
             #   break
        if not elegir:
            print_menu(stdscr, current_row)


curses.wrapper(main)
