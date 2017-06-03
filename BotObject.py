import Constante

class Bot(object):

    def __init__(self, vectorBot):
        self.jugadaBot = vectorBot
        self.gloton = {'posicionX':0, 'posicionY':0, 'fichas':0}

    #esta funcion reiniciara la posicion que tiene mayor cantidad de fichas para comer
    def reiniciarBot(self):
        for posX in range(Constante.DIMENSION):
            for posY in range(Constante.DIMENSION):
                self.jugadaBot[posX][posY]['posicionX'] = 0
                self.jugadaBot[posX][posY]['posicionY'] = 0
                self.jugadaBot[posX][posY]['fichas'] = 0


    # relleno la lista del bot diciendole donde puede comer y cuantas.
    def __cargarJugadaBot(self, tablero, fichaAliada, fichaEnemiga):
        for posX in range(Constante.DIMENSION):
            for posY in range(1, Constante.DIMENSION):
                if (tablero.verificarCasillaValida(fichaAliada, fichaEnemiga, posX, posY)):
                    self.jugadaBot[posX][posY]['posicionX'] = posX
                    self.jugadaBot[posX][posY]['posicionY'] = posY

                    for k in range(Constante.CANTIDAD_DIRECCIONES):
                        self.jugadaBot[posX][posY]['fichas'] += tablero.vectorDireccion[k]['fichasADarVuelta']


    #esta funcion elije la posicion con mayor capacidad de comer fichas enemigas
    def __botGloton(self):
        self.gloton['posicionX'] = 0
        self.gloton['posicionY'] = 0
        self.gloton['fichas'] = 0

        for posX in range(Constante.DIMENSION):
            for posY in range(Constante.DIMENSION):
                if self.jugadaBot[posX][posY]['fichas'] > self.gloton['fichas']:
                    self.gloton['posicionX'] = self.jugadaBot[posX][posY]['posicionX']#recordar que esta invertido el tablero
                    self.gloton['posicionY'] = self.jugadaBot[posX][posY]['posicionY']
                    self.gloton['fichas'] = self.jugadaBot[posX][posY]['fichas']



    def botJuega(self, tablero, fichaAliada, fichaEnemiga):
        self.__cargarJugadaBot(tablero, fichaAliada, fichaEnemiga)
        self.__botGloton()
        tablero.ingresarFicha(self.gloton['posicionX'], self.gloton['posicionY'])

        print 'Jugada del bot:', self.gloton['posicionX'], '', self.gloton['posicionY']
        tablero.dibujar_tablero()