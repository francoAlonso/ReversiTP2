import ExternalCode

RANGO = 10
tablero = [[0 for x in range(RANGO)] for y in range(RANGO)]

tablero = ExternalCode.inicializar_tablero(tablero)
ExternalCode.dibujar_tablero(tablero)