import Constante

class Bot(object):

    def __init__(self):
        self.jugadaBot = [[{'posicionX':0, 'posicionY':0, 'fichas':0} for c in range (Constante.DIMENSION_TABLERO)] for d in range(Constante.DIMENSION_TABLERO)]
        self.gloton = {'posicionX':0, 'posicionY':0, 'fichas':0}

    #esta funcion reiniciara la posicion que tiene mayor cantidad de fichas para comer
    def reiniciarBot(self):
        for posX in range(Constante.DIMENSION_TABLERO):
            for posY in range(Constante.DIMENSION_TABLERO):
                self.jugadaBot[posX][posY]['posicionX'] = 0
                self.jugadaBot[posX][posY]['posicionY'] = 0
                self.jugadaBot[posX][posY]['fichas'] = 0


    # relleno la lista del bot diciendole donde puede comer y cuantas.
    def __cargarJugadaBot(self, tablero, fichaAliada, fichaEnemiga):
        for posX in range(Constante.DIMENSION_TABLERO):
            for posY in range(1, Constante.DIMENSION_TABLERO):
                if (tablero.verificarCasillaValida(fichaAliada, fichaEnemiga, posX, posY)):
                    self.jugadaBot[posX][posY]['posicionX'] = posX
                    self.jugadaBot[posX][posY]['posicionY'] = posY

                    for k in range(Constante.CANTIDAD_DIRECCIONES):
                        self.jugadaBot[posX][posY]['fichas'] += tablero.getFichasADarVuelta(k)


    #esta funcion elije la posicion con mayor capacidad de comer fichas enemigas
    def __botGloton(self):
        self.gloton['posicionX'] = 0
        self.gloton['posicionY'] = 0
        self.gloton['fichas'] = 0

        for posX in range(Constante.DIMENSION_TABLERO):
            for posY in range(Constante.DIMENSION_TABLERO):
                if self.jugadaBot[posX][posY]['fichas'] > self.gloton['fichas']:
                    self.gloton['posicionX'] = self.jugadaBot[posX][posY]['posicionX']#recordar que esta invertido el tablero
                    self.gloton['posicionY'] = self.jugadaBot[posX][posY]['posicionY']
                    self.gloton['fichas'] = self.jugadaBot[posX][posY]['fichas']



    def juega(self, tablero, fichaAliada, fichaEnemiga):
        self.reiniciarBot()
        self.__cargarJugadaBot(tablero, fichaAliada, fichaEnemiga)
        self.__botGloton()
        tablero.invertirFichas(fichaAliada, fichaEnemiga, self.gloton['posicionX'], self.gloton['posicionY'])

        return self.gloton['posicionY'], self.gloton['posicionX']#el tablero esta invertido
