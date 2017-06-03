import Constante
from DireccionObject import VectorDireccion


class Tablero(object):

    contadorTurnos = 0
    juegoTerminado = False

    # constructor, inicializo el tablero con todas sus fichas
    def __init__(self, tablero, cargaVectorDireccion):
        self.tablero = tablero
        self.vectorDireccion = VectorDireccion(cargaVectorDireccion)

        for i in range(Constante.DIMENSION + 1):
            for n in range(Constante.DIMENSION + 1):
                if (i == 0 or i == Constante.DIMENSION):
                    self.tablero[i][n] = chr(48 + n)
                elif (n == 0 or n == Constante.DIMENSION):
                    self.tablero[i][n] = chr(48 + i)
                else:
                    self.tablero[i][n] = Constante.ESPACIO_LIBRE

        tablero[int((Constante.DIMENSION - 1) / 2)][int((Constante.DIMENSION - 1) / 2)] = Constante.FICHA_NEGRA
        tablero[int((Constante.DIMENSION - 1) / 2)][int((1 + Constante.DIMENSION) / 2)] = Constante.FICHA_BLANCA
        tablero[int((1 + Constante.DIMENSION) / 2)][int((Constante.DIMENSION - 1) / 2)] = Constante.FICHA_BLANCA
        tablero[int((1 + Constante.DIMENSION) / 2)][int((1 + Constante.DIMENSION) / 2)] = Constante.FICHA_NEGRA


    #dibujo el tablero
    def dibujar_tablero(self):
        for i in range(Constante.DIMENSION + 1):
            for n in range(Constante.DIMENSION + 1):
                print self.tablero[i][n], ' ',

            print
            print


    # este reinicia el vector direccion para que sea reutilizable
    def reiniciarVectorDireccion(self):
        self.vectorDireccion.reiniciarVectorDireccion()


    # verifica en una unica direccion si es valida. Devuelve un true si lo es.
    def __verificarDireccionValida(self, fichaAliada, fichaEnemiga, i, posX, posY):
        fichasComidas = 0

        if self.tablero[posX][posY] == Constante.ESPACIO_LIBRE and self.tablero[ posX + self.vectorDireccion[i]['direccionX'] ] [posY + self.vectorDireccion[i]['direccionY'] ] == fichaEnemiga:
            fichasComidas += 1
            posX += 2 * self.vectorDireccion[i]['direccionX']
            posY += 2 * self.vectorDireccion[i]['direccionY']

            while (self.tablero[posX][posY] == fichaAliada or self.tablero[posX][posY] == fichaEnemiga) and not self.vectorDireccion[i]['direccionValida']:
                if self.tablero[posX][posY] == fichaEnemiga:
                    fichasComidas += 1
                    posX += self.vectorDireccion[i]['direccionX']
                    posY += self.vectorDireccion[i]['direccionY']
                else:
                    self.vectorDireccion[i]['direccionValida'] = True
                    self.vectorDireccion[i]['fichasADarVuelta'] = fichasComidas

        return self.vectorDireccion[i]['direccionValida']


    # llamara en todas las direcciones a verificar_direccion_valida para devolver una respuesta final si se puede jugar en el casillero
    def verificarCasillaValida(self, fichaAliada, fichaEnemiga, posX, posY):
        casillaValida = False

        for i in range(Constante.CANTIDAD_DIRECCIONES):
            if (self.__verificarDireccionValida(i, fichaAliada, fichaEnemiga, posX,posY)):
                casillaValida = True

        return casillaValida


    # verifica que ambos jugadores tengan la oportunidad de jugar, en caso contrario, saltea su turno
    def sePuedeJugar(self, fichaAliada, fichaEnemiga):
        x = 1
        y = 1
        casillaValida = False

        while (x < Constante.DIMENSION and not casillaValida):
            y = 1
            while (y < Constante.DIMENSION and not casillaValida):
                casillaValida = self.verificarCasillaValida(fichaAliada, fichaEnemiga, x, y)
                y += 1
            x += 1

        return casillaValida

    #llamando a sePuedeJugar, verifica que ambos jugadores juegen. Si ambos no pueden jugar, se termina el juego
    def continuarJuego(self, fichaAliada, fichaEnemiga):
        resultado = False

        if self.sePuedeJugar(fichaAliada, fichaEnemiga):
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
        posX += self.vectorDireccion[i]['direccionX']
        posY += self.vectorDireccion[i]['direccionY']

        while (self.tablero[posX][posY] == fichaEnemiga):
            self.tablero[posX][posY] = fichaAliada
            posX += self.vectorDireccion[i]['direccionX']
            posY += self.vectorDireccion[i]['direccionY']


    # si o si siendo una casilla valida, dara vuelta toda ficha del oponente en la direccion valida.
    def __invertirFichas(self, fichaAliada, fichaEnemiga, posX, posY):
        self.tablero[posX][posY] = fichaAliada

        for i in range(Constante.CANTIDAD_DIRECCIONES):
            if (self.vectorDireccion[i]['direccionValida']):
                self.__invertirFila(i, fichaAliada, fichaEnemiga, posX, posY)


    # la funcion que le permite ingresar al usuario la ficha. Se la pedira hasta que ingrese una casilla valida.
    def ingresarFicha(self, fichaAliada, fichaEnemiga):
        casillero = raw_input('Ingrese dos valoes de 1 a 8 representando las posiciones X e Y: ')
        posX = int(casillero[1])#recordar que el x e y en el tablero esta invertido
        posY = int(casillero[0])

        while (posX < 1 or posX >= Constante.DIMENSION or posY < 1 or posY >= Constante.DIMENSION or not self.verificarCasillaValida(fichaAliada, fichaEnemiga, posX, posY)):
            casillero = raw_input('Posicion no valida, intentelo nuevamente: ')
            posX = int(casillero[1])
            posY = int(casillero[0])

        self.__invertirFichas(fichaAliada, fichaEnemiga, posX, posY)

    #cuenta las fichas del tablero y devuelve la diferencia de fichas ente jugador y bot.
    def contarFichas(self, fichaJugador, fichaBot):
        cantidadFichasJugador = 0
        cantidadFichasBot = 0

        for posX in range(Constante.DIMENSION):
            for posY in range(Constante.DIMENSION):
                if self.tablero[posX][posY] == fichaJugador:
                    cantidadFichasJugador+=1
                elif self.tablero[posX][posY] == fichaBot:
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
