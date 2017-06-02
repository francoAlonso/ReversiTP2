import Constante
from TableroObject import Tablero


#Dimensiones de los objetos.
dimensionTablero = [[0 for x in range(Constante.RANGO_LISTA)] for y in range(Constante.RANGO_LISTA)]
jugadaBot = [{'posicionX':0, 'posicionY':0, 'fichas':0} for o in range (Constante.DIMENSION)]
cargaVectorDireccion = [{'direccionX': 0, 'direccionY':0, 'direccionValida':False, 'fichasADarVuelta':0} for r in range(Constante.CANTIDAD_DIRECCIONES)]

#inicializacion
tablero = Tablero(dimensionTablero, cargaVectorDireccion, jugadaBot)
tablero.dibujar_tablero()

tablero.cargarJugadaBot('N', 'B')

