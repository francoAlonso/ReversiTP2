import ExternalCode

RANGO = 10
tablero = [[0 for x in range(RANGO)] for y in range(RANGO)]
jugadaBot = [{'posicionX':0, 'posicionY':0, 'fichas':0} for o in range (ExternalCode.DIMENSION)]
vectorDireccion = [{'direccionX': 0, 'direccionY':0, 'direccionValida':False, 'fichasADarVuelta':0} for r in range(ExternalCode.CANTIDAD_DIRECCIONES)]

#inicializacion
vectorDireccion = ExternalCode.inicializar_vector_direccion(vectorDireccion)
tablero = ExternalCode.inicializar_tablero(tablero)

ExternalCode.dibujar_tablero(tablero)

casillaValida, vectorDireccion = ExternalCode.ingresar_ficha(tablero, vectorDireccion, 'N', 'B')

print ExternalCode.se_puede_jugar(tablero, vectorDireccion, 'N', 'B')

casillaValida, vectorDireccion = ExternalCode.verificar_casilla_valida(tablero, vectorDireccion, 'N', 'B', 3, 5)
print casillaValida