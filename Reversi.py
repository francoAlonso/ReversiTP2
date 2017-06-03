import Constante
from TableroObject import Tablero
from BotObject import Bot

#Dimensiones de los objetos.
cargaVectorBot = [[{'posicionX':0, 'posicionY':0, 'fichas':0} for c in range (Constante.DIMENSION_TABLERO)] for d in range(Constante.DIMENSION_TABLERO)]

#inicializacion
tablero = Tablero()
jugadaBot = Bot(cargaVectorBot)

fichaJugador, fichaBot = tablero.elegirColorFicha()

#tablero.dibujar_tablero()

tablero.sePuedeJugar('N', 'B')

if fichaJugador == Constante.FICHA_BLANCA:
    jugadaBot.botJuega(tablero, fichaBot, fichaJugador)
