import Constante
from TableroObject import Tablero
from BotObject import Bot

#Dimensiones de los objetos.
dimensionTablero = [[0 for a in range(Constante.RANGO_LISTA)] for b in range(Constante.RANGO_LISTA)]
cargaVectorBot = [[{'posicionX':0, 'posicionY':0, 'fichas':0} for c in range (Constante.DIMENSION)] for d in range(Constante.RANGO_LISTA)]
cargaVectorDireccion = [{'direccionX': 0, 'direccionY':0, 'direccionValida':False, 'fichasADarVuelta':0} for e in range(Constante.CANTIDAD_DIRECCIONES)]

#inicializacion
tablero = Tablero(dimensionTablero, cargaVectorDireccion)
jugadaBot = Bot(cargaVectorBot)

fichaJugador, fichaBot = tablero.elegirColorFicha()

tablero.dibujar_tablero()


if fichaJugador == Constante.FICHA_BLANCA:
    jugadaBot.botJuega(tablero, fichaBot, fichaJugador)
