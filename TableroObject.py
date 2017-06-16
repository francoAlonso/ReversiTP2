import Constante
from DireccionObject import VectorDireccion


class Tablero(object):

    contadorTurnos = 0
    juegoTerminado = False

    # constructor, inicializo el tablero con todas sus fichas
    def __init__(self):
        self.matrizTablero = [[0 for a in range(Constante.RANGO_LISTA)] for b in range(Constante.RANGO_LISTA)]#dimension del tablero
        self.direccion = VectorDireccion()

        for i in range(Constante.DIMENSION_TABLERO + 1):
            for n in range(Constante.DIMENSION_TABLERO + 1):
                if (i == 0 or i == Constante.DIMENSION_TABLERO):
                    self.matrizTablero[i][n] = chr(48 + n)
                elif (n == 0 or n == Constante.DIMENSION_TABLERO):
                    self.matrizTablero[i][n] = chr(48 + i)
                else:
                    self.matrizTablero[i][n] = Constante.ESPACIO_LIBRE

        self.matrizTablero[int((Constante.DIMENSION_TABLERO - 1) / 2)][int((Constante.DIMENSION_TABLERO - 1) / 2)] = Constante.FICHA_NEGRA
        self.matrizTablero[int((Constante.DIMENSION_TABLERO - 1) / 2)][int((1 + Constante.DIMENSION_TABLERO) / 2)] = Constante.FICHA_BLANCA
        self.matrizTablero[int((1 + Constante.DIMENSION_TABLERO) / 2)][int((Constante.DIMENSION_TABLERO - 1) / 2)] = Constante.FICHA_BLANCA
        self.matrizTablero[int((1 + Constante.DIMENSION_TABLERO) / 2)][int((1 + Constante.DIMENSION_TABLERO) / 2)] = Constante.FICHA_NEGRA



    # dibujo el tablero pero previamente borro lo anterior. Tambien esta funcion va a reiniciar el  vector direccion para que sea reutilizable
    def reiniciar(self):
        self.borrarPantalla()

        for i in range(Constante.DIMENSION_TABLERO + 1):#dibujo el tablero
            for n in range(Constante.DIMENSION_TABLERO + 1):
                print self.matrizTablero[i][n], ' ',

            print
            print

        self.resetearVectorDireccion()

    #reinicia el vector direccion para que sea reutilizable
    def resetearVectorDireccion(self):
        self.direccion.reiniciarVectorDireccion()


    # verifica en una unica direccion si es valida. Devuelve un true si lo es.
    def __verificarDireccionValida(self, i, fichaAliada, fichaEnemiga, posX, posY):
        fichasComidas = 0

        if self.matrizTablero[posX][posY] == Constante.ESPACIO_LIBRE and self.matrizTablero[ posX + self.direccion.getOrientacion(i, 'direccionX')][ posY + self.direccion.getOrientacion(i, 'direccionY')] == fichaEnemiga:
            fichasComidas += 1
            posX += 2 * self.direccion.getOrientacion(i, 'direccionX')
            posY += 2 * self.direccion.getOrientacion(i, 'direccionY')

            while (self.matrizTablero[posX][posY] == fichaAliada or self.matrizTablero[posX][posY] == fichaEnemiga) and not self.direccion.getDireccionValida(i) :
                if self.matrizTablero[posX][posY] == fichaEnemiga:
                    fichasComidas += 1
                    posX += self.direccion.getOrientacion(i, 'direccionX')
                    posY += self.direccion.getOrientacion(i, 'direccionY')
                else:
                    self.direccion.setDireccionValida(i, True)
                    self.direccion.setFichasADarVuelta(i, fichasComidas)

        return self.direccion.getDireccionValida(i)


    # llamara en todas las direcciones a verificar_direccion_valida para devolver una respuesta final si se puede jugar en el casillero
    def verificarCasillaValida(self, fichaAliada, fichaEnemiga, posX, posY):
        casillaValida = False

        for i in range(Constante.CANTIDAD_DIRECCIONES):
            if self.__verificarDireccionValida(i, fichaAliada, fichaEnemiga, posX, posY):
                casillaValida = True

        return casillaValida


    # verifica que ambos jugadores tengan la oportunidad de jugar, en caso contrario, saltea su turno
    def sePuedeJugar(self, fichaAliada, fichaEnemiga):
        x = 1
        sePuedeJugar = False

        while (x < Constante.DIMENSION_TABLERO and not sePuedeJugar):
            y = 1
            while (y < Constante.DIMENSION_TABLERO and not sePuedeJugar):
                sePuedeJugar = self.verificarCasillaValida(fichaAliada, fichaEnemiga, x, y)
                y += 1
            x += 1

        return sePuedeJugar

    #llamando a sePuedeJugar, verifica que ambos jugadores juegen. Si ambos no pueden jugar, se termina el juego
    def continuarJuego(self, fichaAliada, fichaEnemiga):
        resultado = False

        if not self.sePuedeJugar(fichaAliada, fichaEnemiga):
            Tablero.contadorTurnos += 1
            resultado = False
        else:
            Tablero.contadorTurnos = 0
            resultado = True

        if Tablero.contadorTurnos == 2:
            Tablero.juegoTerminado = True

        return resultado

    # El encargado de invertir las fichas del opoenente pero en una unica direccion
    def __invertirFila(self, i, fichaAliada, fichaEnemiga, posX, posY):
        posX += self.direccion.getOrientacion(i, 'direccionX')
        posY += self.direccion.getOrientacion(i, 'direccionY')

        while (self.matrizTablero[posX][posY] == fichaEnemiga):
            self.matrizTablero[posX][posY] = fichaAliada
            posX += self.direccion.getOrientacion(i, 'direccionX')
            posY += self.direccion.getOrientacion(i, 'direccionY')


    # si o si siendo una casilla valida, dara vuelta toda ficha del oponente en la direccion valida.
    def invertirFichas(self, fichaAliada, fichaEnemiga, posX, posY):
        self.matrizTablero[posX][posY] = fichaAliada

        for i in range(Constante.CANTIDAD_DIRECCIONES):
            if (self.direccion.getDireccionValida(i)):
                self.__invertirFila(i, fichaAliada, fichaEnemiga, posX, posY)


    # esta funcion devuelve la posicion ingresada por el usuario. Verifica que solo sean numeros
    def verificarNumeros(self):
        while True:
            try:  # los try and catch me van a negar el ingreso de letras.
                casillero = raw_input('Ingrese dos valoes de 1 a 8 representando las posiciones X e Y: ')
                posX = int(casillero[1])  # recordar que el x e y en el tablero esta invertido
                posY = int(casillero[0])
                break
            except:
                print "Ingrese solo numeros"

        return posX, posY

    # la funcion que le permite ingresar al usuario la ficha. Se la pedira hasta que ingrese una casilla valida.
    def ingresarFicha(self, fichaAliada, fichaEnemiga):
        posX, posY = self.verificarNumeros()

        while not self.verificarCasillaValida(fichaAliada, fichaEnemiga, posX, posY):
            posX, posY = self.verificarNumeros()

        self.invertirFichas(fichaAliada, fichaEnemiga, posX, posY)


    #cuenta las fichas del tablero y devuelve la diferencia de fichas ente jugador y bot.
    def contarFichas(self, fichaJugador, fichaBot):
        cantidadFichasJugador = 0
        cantidadFichasBot = 0

        for posX in range(Constante.DIMENSION_TABLERO):
            for posY in range(Constante.DIMENSION_TABLERO):
                if self.matrizTablero[posX][posY] == fichaJugador:
                    cantidadFichasJugador+=1
                elif self.matrizTablero[posX][posY] == fichaBot:
                    cantidadFichasBot+=1

        return cantidadFichasJugador-cantidadFichasBot

    #le da al jugador la oportunidad de elegir que ficha quere ser
    def elegirColorFicha(self):
        fichaEnemiga = ''
        fichaAliada = ''

        while (fichaAliada != Constante.FICHA_BLANCA and fichaAliada != Constante.FICHA_NEGRA):
            fichaAliada = raw_input('Ingrese una Color entre N o B: ').upper()

        if fichaAliada == Constante.FICHA_NEGRA:
            fichaEnemiga = Constante.FICHA_BLANCA
        else:
            fichaEnemiga = Constante.FICHA_NEGRA

        return fichaAliada, fichaEnemiga


    def getFichasADarVuelta(self, posicion):
        return self.direccion.getFichasADarVuelta(posicion)

    #esta funcion me permite dar el efecto de borrar la pantalla
    def borrarPantalla(self):
        print '\n' * 50
