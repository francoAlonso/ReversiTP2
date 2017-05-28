DIMENSION = 9
FICHA_NEGRA = 'N'
FICHA_BLANCA = 'B'
ESPACIO_LIBRE = '_'
CANTIDAD_DIRECCIONES = 8

#esta funcion se llama una unica vez y recibe el tablero en blanco, donde los rellenariamos con las fichas iniciales del juego.
def inicializar_tablero(tablero):
    for i in range(0,DIMENSION+1):
        for n in range(0,DIMENSION+1):
            if(i==0 or i==9):
                tablero[i][n] = chr(48 + n)
            elif(n==0 or n==DIMENSION):
                tablero[i][n] = chr(48 + i)
            else:
                tablero[i][n] = ESPACIO_LIBRE

    tablero[ (DIMENSION-1)/2 ][ (DIMENSION-1)/2 ] = FICHA_NEGRA
    tablero[ (DIMENSION-1)/2 ][ (1+DIMENSION)/2 ] = FICHA_BLANCA
    tablero[ (1+DIMENSION)/2 ][ (DIMENSION-1)/2 ] = FICHA_BLANCA
    tablero[ (1+DIMENSION)/2 ][ (1+DIMENSION)/2 ] = FICHA_NEGRA

    return tablero

#una vez inicializado el tablero, va a imprimirlo para que el usuario vea el estado actual.
def dibujar_tablero(tablero):
    for i in range(0,DIMENSION+1):
        for n in range(0, DIMENSION+1):
            print tablero[i][n], ' ',

        print
        print