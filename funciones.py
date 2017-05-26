DIMENSION = 9
FICHA_NEGRA = 'N'
FICHA_BLANCA = 'B'
ESPACIO_LIBRE = '_'
CANTIDAD_DIRECCIONES = 8

def inicializar_tablero(tablero):
    for i in range(0,DIMENSION+1):
        for n in range(0,DIMENSION+1):
            if(i>0 and i<9):
                tablero[i,n]= ESPACIO_LIBRE
            else:
                tablero[i,n] = chr(48+n)

            if(n>0 and n<9):
                tablero[i,n] = ESPACIO_LIBRE
            else:
                tablero[i,n] = chr(48+i)

    tablero[(DIMENSION-1)/2,(DIMENSION-1)/2] = FICHA_NEGRA
    tablero[(DIMENSION-1)/2,(1+DIMENSION)/2] = FICHA_BLANCA
    tablero[(1+DIMENSION)/2,(DIMENSION-1)/2] = FICHA_BLANCA
    tablero[(1+DIMENSION)/2,(1+DIMENSION)/2] = FICHA_NEGRA

    return tablero

def dibujar_tablero(tablero):
    for i in range(0,DIMENSION+1):
        for n in range(0, DIMENSION+1):
            print(tablero[i,n], ' ')
            print()
            print()